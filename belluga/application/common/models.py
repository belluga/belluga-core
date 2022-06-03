def ResponseModel(data: dict = None, message: str = None, page: int = None, count: int = None):
    response = {}
    if (data != None):
        response["data"] = data

    if (message != None):
        response["message"] = message
    
    if (page != None):
        response["page"] = page
    
    if (count != None):
        response["count"] = count
    
    return response


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}