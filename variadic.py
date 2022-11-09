def a_sum(a, b, x, *args, **kwargs):
    print(args)
    print(kwargs)


a_sum(1, 2, 10, 23, 65, 2, y=6, asd=456)
