def div(a, b):
    return a/b


result = div(6, 3)

# pod maską asercji
# if result == 2.0:
#     print("PASSED")
# else:
#     raise Exception("FAILED")


assert div(6, 3) == 2, "FAILED"
print("PASSED")

assert div(10, 2) == 5, "FAILED"
print("PASSED")
