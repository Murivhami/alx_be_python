#!/bin/bash
#Class definition.
class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance


    def deposit(self, amount):
        return amount + self.account_balance

    def withdraw(self, amount):
        if amount > self.account_balance:
            return(f"{self.account_balance}")
        else:
            return self.account_balance - amount

    def display_balance(self):
        return(f"Current Balance: {self.account_balance}")

my_bankaccount = BankAccount(10000)
print(my_bankaccount.withdraw(12000))
