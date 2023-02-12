from firebase_utils.firebase_authentication import credentials_check
from utils.request_handler import request_handler


def main(request):

    # Get JSON and convert to Dictionary
    request_json = request.get_json(silent=True)

    # request_handler will validate contents of request
    handler_result = request_handler(request_json)

    if handler_result is not True:
        return handler_result

    # If all tests pass in request_handler get the user and password
    user = request_json["email"]
    pw = request_json["password"]

    # Check that the user exists in Firebase
    if credentials_check(user, pw) is True:
        print("User Exists")
        # call compute cloud function here
    else:
        print("User doesn't exist")

    return "Code ran to completion Successfully", 200
