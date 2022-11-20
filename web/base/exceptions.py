from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError

def ExceptionHandler(exc, context):
    response = exception_handler(exc, context)
    result = {"error":""}
    if response.data.get("non_field_errors"):
        response.data = {"error":response.data["non_field_errors"]}
    else:
        response.data = {"error":response.data}
    response.data["result"] = ""
    return response 