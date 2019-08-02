class Customers:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

    def getBalance(self):
        return self.balance

if __name__ == '__main__':
    customer1 = Customers('Wafa',1000000)

    while True:
        option = int(input("Please Enter your Choice\n1- press #1 for Deposit\n2- press #2 for Withdraw\n3- press #3 to check balance\n4- press #0 for exit application\n Your choice is : "))

        if option == 1:
            deposit_amount =float(input("Please ente the deposit amount: "))
            if deposit_amount >= 0:
                current_balance = customer1.deposit(deposit_amount)
                print('The Current Balance after deeposit is: ',current_balance)
            else:
                print("The deposit amount must be greater than zero")
        elif option == 2:
            withdraw_amount = float(input("Please the withdraw amount: "))
            current_balance = customer1.getBalance()
            if withdraw_amount >= 0:
                if current_balance >= withdraw_amount:
                    new_balance = customer1.withdraw(withdraw_amount)
                    print("The current balance after withdraw is: ",new_balance)
                else:
                    print("The withdraw amount must be lees than or equal your current balance")
            else:
                print("The withdraw amount must be lees than or equal zero")
        elif option == 3:
            current_balance= customer1.getBalance()
            print("The current balance is: ",current_balance)
        elif option == 0:
            break
        else:
            print("Please enter coorect choice")

