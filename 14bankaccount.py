# 10/26/2018
# Bank Account!

class Bank:
	def __init__(self, name, pin, balance, accNumber):
		self.name = name
		self.pin = pin
		self.balance = balance
		self.accNumber = accNumber

	def withdraw(self, balance):
		status = ""
		if self.balance > 0:
			self.balance -= amount1
			statusWithdraw = self.name + " just took out a lot of money!"
		else:
			statusWithdraw = self.name + " can't take out any more money!"
		return statusWithdraw

	def deposit(self, balance):
		status = ""
		if self.balance <5000000:
			self.balance += amount2
			statusDeposit = self.name + " just put in a lot of money!"
		else:
			statusDeposit = self.name + " can't put in any more money!"
		return statusDeposit

	def stats(self):
		return "\nName: " + self.name + "\nPin Number: " + str(self.pin) + "\nAccount Number: " + str(self.accNumber) + "\nBalance: " + "$" + str(self.balance)

# def checkBalance(self, balance):

# transfer

# createAccount


pin = input("\n\nWelcome to your bank! You can create an account by inputting a 4-digit numerical pin number: ")
name = input("What is your name?\n")
# print("Your pin number is: " + pin)
account = Bank(name, pin, 5076, 1000000)

while True:
	print(account.stats())
	choice = input("\n\nWhat do you want to do with your account?\n")

	if choice == "Withdraw":
		amount1 = input("How much would you like to withdraw?: ")
		print(account.withdraw(amount1))
	
	elif choice == "Deposit":
		amount2 = input("How much would you like to deposit?: ")
		print(account.deposit(amount2))
	else:
		print("You can't do that!")




