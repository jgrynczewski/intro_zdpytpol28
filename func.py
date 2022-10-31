def even_numbers(num):
    print(f"Liczby parzyste mniejsze od {num} to:")
    i = 0
    while i < num:
        if i % 2 == 0:
            print(i)
        i += 1


res = int(input("Podaj liczbę: "))
even_numbers(res)

