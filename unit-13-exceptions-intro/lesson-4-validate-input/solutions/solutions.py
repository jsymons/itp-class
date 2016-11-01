def validate_int(param):
    if not isinstance(param, (int)):
        raise TypeError
    else:
        return param