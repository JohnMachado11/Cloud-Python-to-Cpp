import re


def request_handler(data):
    """
    Parses the contents of the request data
    :return: String + Int or Boolean
    """

    def email_validator(email):
        """
        Check that the email is in the
        correct format of "name@email.com
        :return: Boolean
        """

        email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        def is_valid_email(email):
            if email_regex.match(email):
                return True
            else:
                return False

        return is_valid_email(email)

    # Check that the contents of "data" is not empty and that the correct keys are present  
    if data is None or set(data.keys()) != {"email", "password"}:
        return "Invalid JSON data", 400

    # Check that the data type of the email is a string
    if not isinstance(data["email"], str):
        return "Invalid email format", 400

    # Check that the email is in the correct format of "name@email.com"
    if email_validator(data["email"]) is False:
        return "Invalid email format", 400

    # Check that the data type of the password is a string
    if not isinstance(data['password'], str):
        return "Password should be a string", 400

    # Add decrypt here for password

    return True
