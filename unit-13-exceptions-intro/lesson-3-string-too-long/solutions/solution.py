def string_too_long(input):
    if len(input) > 10:
        raise ValueError("String is too long :c")
    else:
        return False
