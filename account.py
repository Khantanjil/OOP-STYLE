# Object Oriented Programming
# OOP POO

# Create a class


class Account(object):

    # DocString
    """
Docstrings  here:
This is a OOP (object oriented programming) on python.
The class is a bank account.
    """
    # Constructor
    def __init__(self, filepath, username, password, email):
        self.filepath = filepath
        self.username = username
        self.password = password
        self.email = email
        
        # Read the balance
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    # Method
    # Show to current balance on the account
    def showQuantity(self):
        """
        Return the current balance on your account.
        """
        return f"{self.username}'s account: {self.balance}"


    # Method to withdraw the money
    def withdraw(self, amount):
        """
        Method which you need to pass the amount of money to withdraw
        """
        self.balance = self.balance - amount

    # Method to deposit the money
    def deposit(self, amount):
        """
        Method which you need to pass the amount of money to deposit on the bank account
        """
        self.balance = self.balance + amount

    # Save the changes
    def commit(self):
        """Save the changes"""
        with open(self.filepath, 'r+') as file:
            file.write(str(self.balance))

    # Represation of the object
    def __repr__(self):
        return f"Your email is {self.email}.\nYour username is {self.username}.\nYour password is {self.password}\nYour current balance is {self.balance}"

# Objects
tanjil_account = Account("tanjil_account.txt", "tanjil", "omneteesuhfevtS", "tanjilkhan.sh@gmail.com")
print(tanjil_account)

