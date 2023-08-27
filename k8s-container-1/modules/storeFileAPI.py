from flask import Blueprint,request
from modules.shared.validateData import validateBody
import pandas as pd
import os
from datetime import datetime

store_file_api_bp = Blueprint('storeFile',__name__)

@store_file_api_bp.route('',methods=['POST'])
def store_file():
    content_type = request.headers.get("Content-Type")
    if content_type == 'application/json':
        json_data = request.json
        required_keys = ['file','data']
        required_keys = set(required_keys)
        json_keys_set = set(json_data)
        
        result = {'file':None}
        if required_keys == json_keys_set:
            result['file'] = json_data['file']
            isBodyValidated = validateBody(json_data)
            if isBodyValidated:
                isSaved = saveStringToCSV(json_data['data'],json_data['file'])
                if isSaved:
                    result["message"] = "Success."
                else:
                    result["error"] = "Error while storing the file to the storage."
            else:
                result['error'] = "Invalid JSON input."
        else:
            result['error'] = "Invalid JSON input."

    return result


@store_file_api_bp.route('/ping',methods=['GET'])
def ping():

    return {"message": "PONG " + datetime.now().isoformat()}

def saveStringToCSV(data,file_name):

    rows = data.split('\n')
    columns = [column.strip() for column in rows[0].split(', ')]
    data_list = []    
    for row in rows[1:]:
        data_list.append([cell.strip() for cell in row.split(', ')])

    df = pd.DataFrame(data_list, columns=columns)
    df.to_csv(f"/usr/files/{file_name}",index=False)
    return os.path.exists(f"/usr/files/{file_name}")

