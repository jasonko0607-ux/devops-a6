def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def greeting(name):
    return f"Hi, {name}! Welcome to DevOps."


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
