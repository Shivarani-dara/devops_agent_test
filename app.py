
def add_numbers(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        raise TypeError('Both arguments must be numbers')
        

if __name__ == '__main__':
    add_numbers(2,9)