# Dla zadanego słowa oblicz jego wartość punktową w grze scrabble.
# Przyjmij słownik zawierający punkację dla poszczególnych liter.

points = {
    'a': 1,
    'b': 3,
    'l': 2,
}

word = input('Podaj słowo: ')

result = 0
for char in word:
    char_value = points[char]
    result += char_value

print(f"Słow {word} jest warte {result} pkt.")
