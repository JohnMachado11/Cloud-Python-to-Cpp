from firebase_utils.firebase_config import config
from requests.exceptions import HTTPError
import pyrebase


def credentials_check(email, password):
    """ 
    Check the users email and password to see
    if they exist as a user in Firebase
    :return: Boolean
    """

    def init_firebase_app():
        """
        Initialize Firebase application and 
        authenticates with Firebase Authentication
        :return: Pyrebase Auth object
        """

        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()

        return auth

    auth = init_firebase_app()

    try:
        auth.sign_in_with_email_and_password(email, password)
        return True
    except HTTPError:
        print("Incorrect Credentials")
        return False
