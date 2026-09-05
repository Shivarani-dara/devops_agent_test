
def add_numbers(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return int(a) + int(b)
    else:
        return a + b

if __name__ == '__main__':
    add_numbers(2,9)