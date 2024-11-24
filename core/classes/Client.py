from abc import ABC  # модул за абстрактни класове


class Client(ABC):
    def __init__(self, name, age, egn, iban, phone_number):
        self.name = name
        self.age = age
        self._egn = egn  # private
        self.iban = iban
        self._phone_number = phone_number  # private

    # setter/getter за променливите на класа
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age

    @property
    def egn(self):
        return self._agent

    @egn.setter
    def egn(self, egn):
        self._egn = egn

    @property
    def iban(self):
        return self.iban

    @iban.setter
    def iban(self, iban):
        self.iban = iban

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def increase_age(self):
        self.age += 1

    def __str__(self):
        return f'{self.name},{self.age},{self.egn},{self.iban},{self.phone_number}'
