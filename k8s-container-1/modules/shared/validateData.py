def validateBody(body):
    flag = True
    for value in body.values():
        if not (type(value) == str and len(value) > 0):
            flag = False
            break    
    return flag