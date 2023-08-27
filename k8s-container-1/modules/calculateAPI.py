from flask import Blueprint,request
from modules.shared.validateData import validateBody
import requests
calculate_api_bp = Blueprint('calculate',__name__)

@calculate_api_bp.route('',methods=['POST'])
def calculate():
    content_type = request.headers.get("Content-Type")
    if content_type == 'application/json':
        json_data = request.json
        required_keys = ['file','product']
        required_keys = set(required_keys)
        json_keys_set = set(json_data)
        result = {'file':None}
        if json_keys_set == required_keys:
            result['file'] = json_data['file']
            isBodyValidated = validateBody(json_data)
            if isBodyValidated:
                response = requests.post("http://localhost:7000/summation/csv",headers={"Content-Type":"application/json"},json=json_data)
                if response.status_code == 200:
                    result = response.json()
                else:
                    result['error'] = f'Server Issue: Status Code {response.status_code}'
            else:
                result['error'] = "Invalid JSON input."
        else:
            result['error'] = "Invalid JSON input."

    return result


