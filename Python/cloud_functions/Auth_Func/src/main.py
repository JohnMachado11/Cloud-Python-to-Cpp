from firebase_utils.firebase_authentication import credentials_check
from utils.request_handler import request_handler
from utils.compute_caller import call_compute_func


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

    # Maybe add decrypt here for password

    # Check that the user exists in Firebase
    if credentials_check(user, pw) is True:
        print("User Exists, calling Compute_Func Cloud Function\n")
        
        # Compute_Func Cloud Function called
        data = call_compute_func()
    else:
        print("User doesn't exist")
        return "User Not Found", 404

    return data, 200
