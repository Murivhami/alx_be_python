#!/bin/bash
#Class definition.
class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance


    def deposit(self, amount):
        if amount > 0:
            return amount + self.account_balance

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"

#my_bankaccount = BankAccount(10000)
#print(my_bankaccount.withdraw(12000))
