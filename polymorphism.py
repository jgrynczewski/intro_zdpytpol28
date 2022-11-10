# Polimorfizm/wielopostaciowość

# A. polimorficzna metoda (dzięki duck typing)
class Dog:
    def speak(self):
        print("Hau hau hau")


class Cat:
    def speak(self):
        print("Miau miau miau")


class Cow:
    def speak(self):
        print("Muu Muu Muuuu")


dog = Dog()
cat = Cat()
cow = Cow()

home_zoo = [dog, cat, cow]

for animal in home_zoo:
    animal.speak()  # tutaj widzimy polimorfizm metody speak


# B. polimorficzna funkcja
staffs = ["ala", Cow, 3, False]

for staff in staffs:
    print(staff)  # tutaj widzimy polimorfizm funkcji print
