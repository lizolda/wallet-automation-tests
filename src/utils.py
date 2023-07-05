from datetime import datetime


expiration_date_format = "%m / %y"


def get_expiration_from_date_to_input_string(expiration):
    return expiration.strftime(expiration_date_format)


def expiration_from_string(raw_input):
    return datetime.strptime(raw_input, expiration_date_format)
