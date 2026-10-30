
def add_numbers(a, b):
    try:
        return a + int(b)
    except ValueError:
        raise TypeError('Both arguments must be numbers')

if __name__ == "__main__":
    add_numbers(2,9)# Webhook integration test and also we wanna check
