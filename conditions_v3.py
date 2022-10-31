x = 5

if x:  # tu zachodzi niejawna konwersja wartości na typ bool
    print("foo")


# Promocja typów
print(2 + 2.0)  # koercja - (niejawna konwersja wartości na inny typ)

# falsy (wartości fałszywe - wartości, które po zrzutowaniu na boolean dają False)
# 0, 0.0, 0+0j, False, None, ""

# truthy (prawdziwe)