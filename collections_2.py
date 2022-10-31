# LBYL - Look Before You Leap (prewencja)
# EAFP - Easier Ask Forgiveness Than Permission (leczenie)

# EAFP
def get_area(r):
    try:
        return 3.14 * r**2
    except TypeError:
        print("Podana wartość nie jest numeryczna")
        return 0


res = get_area(-10)
print(res)

