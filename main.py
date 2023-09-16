class BankAccount:
    def __init__(self,account_holder_name,account_number,balance):
        self.__account_holder_name=account_holder_name
        self.__account_number=account_number
        self.__account_balance=balance

    def deposite(self,amount):
        if(amount>0):
            self.__account_balance+=amount
            print("deposite amount Rs:{}, and Current balance after deposite Rs:{}".format(amount,self.__account_balance))
        else:
            print("Invalid deposite, Please try again")
    def withdraw(self,amount):
        if (amount>0 and self.__account_balance>=amount):
            self.__account_balance-=amount
            print("Withdraw Amount Rs:{}, and Current balance after withdraw Rs:{}".format(amount,self.__account_balance))
        else:
            print("Invalid Withdraw Ammount. Please try again")

    def checkbalance(self):
        print("Account Holder Name :{}, Your Account Number :{}, Your Current Balance Rs:{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))


name=input("Enter Account Holder name :")
accno=int(input("Enter Account Number :"))
accbal=float(input("Enter Current Balance :"))
