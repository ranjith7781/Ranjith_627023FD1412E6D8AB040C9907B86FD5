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

a=BankAccount(name,accno,accbal)
print(" 1.Deposite Ammount \n 2.Withdraw Ammount \n 3.Check Balance \n 4.Exit")
n=int(input("Please Enter any choice :"))
if(n==1):
      amount=float(input("Enter Deposite amount :"))
      a.deposite(amount)
elif(n==2):
    wamount=float(input("Enter Withdraw Amount :"))
    a.withdraw(wamount)
elif(n==3):
    a.checkbalance()
elif(n==4):
    print("Thankyou for visiting....")
else:
    print("Sorry wrong choice.......")