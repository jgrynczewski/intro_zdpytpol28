# Enkapsulacja/hermetyzacja/kapsułkowanie (data hiding)

# Modyfikator dostępu (access modifiers)
#  atrybut/metoda publiczna (pole)
# _ - atrybut/metoda chroniona (pole)
# __ - atrybut/metoda prywatna (pole)

# property

# class Account:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     # setter
#     def set_balance(self, new_balance):
#         if type(new_balance) != int or new_balance < 0:
#             print("Podano nieprawidłową wartość")
#         else:
#             self.__balance = new_balance
#
#     # getter
#     def get_balance(self):
#         return self.__balance
#
#     balance = property(get_balance, set_balance)

##############################################

# a = Account(100)
# print(a.get_balance())
# a.set_balance(250)
# print(a.get_balance())
# a.set_balance(-200)
# print(a.get_balance())
# a.set_balance("ala")
# print(a.get_balance())

# print(a.balance)
# a.balance = 250
# print(a.balance)
# a.balance = -200
# print(a.balance)
# a.balance = "ala"
# print(a.balance)


class Account:
    def __init__(self, balance):
        self.__balance = balance

    # getter
    @property
    def balance(self):
        return self.__balance

    # setter
    @balance.setter
    def balance(self, new_balance):
        if type(new_balance) != int or new_balance < 0:
            print("Podano nieprawidłową wartość")
        else:
            self.__balance = new_balance


a = Account(100)
print(a.balance)
a.balance = 250
print(a.balance)
a.balance = -200
print(a.balance)
a.balance = "ala"
print(a.balance)
