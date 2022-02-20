import os


def get_username():
    username = os.getenv("ENV_USERNAME")

    if username is None:
        raise OSError("USERNAME environment is not set.")

    return username.lower()


def get_password():
    password = os.getenv("ENV_PASSWORD")

    if password is None:
        raise OSError("PASSWORD environment is not set.")

    return password


def get_invalid_username():
    invalid_username = os.getenv("INVALID_USERNAME")

    if invalid_username is None:
        raise OSError("INVALID_USERNAME environment is not set.")

    return invalid_username.lower()


def get_invalid_password():
    invalid_password = os.getenv("INVALID_PASSWORD")

    if invalid_password is None:
        raise OSError("INVALID_PASSWORD environment is not set.")

    return invalid_password
