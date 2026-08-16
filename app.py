def add_numbers(a, b):
    try:
        return int(a) + int(b)
    except TypeError:
        raise ValueError('Both arguments must be numbers')