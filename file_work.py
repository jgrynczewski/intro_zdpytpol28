# ODCZYT
# f = open('text.txt', encoding='utf-8')

# Wczytywanie całej zawartości pliku
# Sposób 1 - jako str
# content = f.read()
# Sposób 2 - jako lista
# content = f.readlines()

# Wczytywanie linijka po linijce
# Sposób 1
# while True:
#     line = f.readline()
#     if line == '':
#         break
#     print(line, end='')

# Sposób 2
# for line in f:
#     print(line, end='')

# f.close()

# ZAPIS (NADPISANIE)
f = open('text.txt', 'w', encoding='utf-8')

f.write("Pies ma kość\n")
f.write("Ala ma kota\n")

f.close()

# ZAPIS (UZUPEŁENIENIE)
f = open('text.txt', 'a', encoding='utf-8')

f.write("Pies ma kość\n")

f.close()
