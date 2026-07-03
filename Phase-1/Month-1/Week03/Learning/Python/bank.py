# Some Exersices (Day 13)
from random import randint


class Bank:
    account_id = 0
    def __init__(self, name,password,balance):
        self.name = name
        self._password = password
        self.balance = balance
        self.account_id = str(Bank.account_id).zfill(4)

        account_number = str(randint(1,9999))
        for i in range(3):
           account_number += "-" + str(randint(1,9999)) 
        self.__account_number = account_number

        Bank.account_id += 1

    def __str__(self):
        return f"Your name is {self.name}. You have in your credit card {self.balance}."
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_pass):
        self._password = new_pass
    
test = Bank("hi", "ok", 0)
print(test.password)

print(test)

test.password = "Aliens"
print(test.password)
