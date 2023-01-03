def add(x, y):
    return x + y

def substract(x, y):
    return x - y

# print(add(4, 5))    # => 9 {mauvaise pratique}

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("cannot divide by zero!")
    return x / y