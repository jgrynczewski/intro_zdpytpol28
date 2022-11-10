def add(x, y):
    return x + y


def product(x, y):
    return x * y


def is_palindrom(string):
    return string.lower().replace(" ", "") == string[::-1].lower().replace(" ", "")
