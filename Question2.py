class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print("Current balance:", self.__balance)


account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

account.display_balance()
