# BANK MANAGEMENT SYSTEM - Common Big Program (100 Marks)

class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} Deposited. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} Withdrawn. Remaining: ₹{self.balance}")
        else:
            print("Insufficient Balance! Like your refund case - money varala")

    def display(self):
        print(f"Acc No: {self.acc_no} | Name: {self.name} | Balance: ₹{self.balance}")

# Main Program
accounts = {}

while True:
    print("\n--- BANK MENU ---")
    print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Display\n5. Exit")
    ch = input("Enter Choice: ")

   
