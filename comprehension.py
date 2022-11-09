# # List comprehension
# # old fasion way
# new_list = []
# for item in range(10):
#     if item % 2 == 0:
#         new_list.append(item**2)

# # new fasion - list comprehension
# new_list = [item**2 for item in range(10) if item % 2 == 0]
#
# print(new_list)

# # Dict comprehension
# old-fasion way
# words = ["ala", 'eustachy', 'papuga', 'samochód']
# new_dict = {}
# for word in words:
#     new_dict[word] = len(word)

# new-fasion dict comprehension
# new_dict = {word: len(word) for word in words}

# print(new_dict)

# # Set comprehension
# # old-fasion way
words = ["ala", 'eustachy', 'papuga', 'samochód']
# new_set = set()
#
# for word in words:
#     new_set.add(len(word))

# # new-fasion way
new_set = {len(word) for word in words}

print(new_set)
