class ATM:
	def __init__(self, amount):
        self.amount = amount
    def check(self):
        return f"You have ${self.amount} in your account"
    def deposit(self):
        return f"Successfully deposited ${self.amount}"
    def withdraw(self):
        return f"Successfully withdrew ${self.amount}"

deposits = []
withdrawals = []
print("Welcome to the ATM\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
while True:
    balance = sum(deposits) - sum(withdrawals)
    option = input("Please choose an option: ")
    if option == '1':
        transaction = ATM(balance)
        print(transaction.check())
    elif option == '2':
        money = int(input("Enter amount to deposit: "))
        deposits.append(money)
        transaction = ATM(money)
        print(transaction.deposit())
    elif option == '3':
        money = int(input("Enter amount to withdraw: "))
        withdrawals.append(money)
        transaction = ATM(money)
        print(transaction.withdraw())
    elif option == '4':
        print("Program closed")
        break
    else:
        print("Invalid option")
