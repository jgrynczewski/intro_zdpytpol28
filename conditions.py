number = int(input("Proszę, podaj liczbę: "))
if number < 0:
    print("Sorry, brak rozwiązań w zbiorze liczb rzeczywistych.")
else:
    result = f"Pierwiastek podanej liczby wynosi: {number**(1/2)}"
    print(result)
