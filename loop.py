num = int(input("Podaj liczbę: "))
i = 0

while True:
    i += 1

    if i == num:
        break

    if i % 2 != 0:
        continue

    print(i)
