def deco(func):
    def modified_func():
        print("Dekoruję przed")
        func()
        print("Dekoruję po")

    return modified_func


@deco
def hello():
    print("hello")


# hello = deco(hello)
hello()
