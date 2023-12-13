def identity(*args):
    return args


def cast_str(*args):
    return tuple(map(str, args))
