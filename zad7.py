words = {}

with open('oda.txt', encoding='utf-8') as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1

print(words)
