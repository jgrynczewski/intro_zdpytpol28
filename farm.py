class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello!")

    def run(self):
        print("Biegnę")


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.is_alive = True

    def speak(self):
        print("Muuuuu!")

    def introduce(self):
        if self.is_alive:
            print(f"Cześć, jestem krową o imieniu {self.name} i mam {self.age} lat.")
        else:
            print("Niestety nie żyję. Chcesz poznać moje imię? To mnie wskrzesz!")

    def get_area(self, r):
        return 3.14 * r**2

    def get_older(self):
        self.age += 1

    def get_younger(self):
        self.age -= 1

    def kill(self):
        print(f"{self.name}: Zabijam się...")
        self.is_alive = False

    def resurrect(self):
        print(f"{self.name}: Wskrzeszam się...")
        self.is_alive = True

    # rozszerzenie metody rodzica
    def run(self):
        super().run()
        print("Ale szybko się męczę")

    def __str__(self):
        return f"Cow: {self.name}"


class Dog(Animal):
    def speak(self):
        print("Hau hau")


class Cat(Animal):
    def speak(self):
        print("Miauuuuuuuu")

    # nadpisywanie metody rodzica
    def run(self):
        print("Stąpam majestatycznie")


class Farmer:
    def __init__(self, name, house, child_name):
        self.name = name
        self.child = Child(child_name)  # asocjacja (agregacja+tworzenie)
        self.house = house  # agregacja

    def introduce(self):
        print(f"{self.name}: Cześć, jestem farmer {self.name} i mieszkam {self.house}!")

    def kill_cow(self, cow):
        cow.kill()
        print(f"{self.name}: Hahaha, zabiłem krowę {cow.name}.")

    def count_eggs(self, chick):
        return len(chick.eggs)


class House:
    def __init__(self, address):
        self.address = address
        self.is_lit = False

    def ignite(self):
        self.is_lit = True


class Child:
    def __init__(self, name):
        self.name = name


class Chick:
    def __init__(self, name):
        self.name = name
        self.eggs = []

    def make_egg(self):
        egg = Egg()
        self.eggs.append(egg)


class Egg:
    pass


##############################################################

c1 = Cow("Mućka", 5)
c2 = Cow("Milka", 2)

c1.introduce()

res = c1.get_area(10)
print(f"Krowa powiedziała, że pole koła to {res}")

print(c1.age)
c1.get_older()
print(c1.age)
c1.get_younger()
print(c1.age)

c1.introduce()
c1.kill()
c1.introduce()
c1.resurrect()
c1.introduce()

c1.say_hello()

k = Cat('Filemon', 1)
d = Dog('Burek', 6)

k.speak()
d.speak()

k.say_hello()

print("######### Pies #############")
d.run()  # dziedziczy
print("######### Kot #############")
k.run()  # nadpisuje
print("######### Krowa #############")
c1.run()  # rozszerza

h1 = House('Konwaliowa 32')

f = Farmer(name="Donald", house=h1, child_name='Stasio')
f.introduce()
f.kill_cow(c2)


c = Chick('Nioska')
c.make_egg()
c.make_egg()
c.make_egg()

print(c.eggs)

print(f.count_eggs(c))
