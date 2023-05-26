import random
class Account:
    def __init__(self,number, name, cpf, balance = 0):
        self._acc_number = "314{}00125".format(number)
        self._acc_name = name
        self._acc_cpf = cpf
        self._acc_balance = balance

    @property
    def name(self):
        return self._acc_name

    @property
    def balance(self):
        return self._acc_balance

    def outdraw(self, value):
        self._acc_balance -= value

    def deposit(self, value):
        self._acc_balance += value

    def change_name(self, new_name):
        self._acc_name = new_name