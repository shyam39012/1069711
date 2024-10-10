from datetime import datetime,date
from collections import defaultdict
i=1020304050
database={}
list_accounts=[]
transactions=defaultdict(dict)
while(True):
    class BankApplication:
        def createAccount(self,i):
            self.name=input("Enter your name: ")
            self.phoneNo=int(input("Enter your contact number: "))
            self.address=input("enetr your address details:")
            self.amount=0
            self.account_no=i
            database[self.account_no]={"Account Number":self.account_no,"name":self.name,"Phone number":self.phoneNo,"Address":self.address,"Amount":self.amount}
            return self.account_no
        def ViewAccountDetails(self,account_number):
            print(database[account_number])
        def Withdraw(self,account_number):
            money=int(input("enter amount to withdraw: "))
            current_date=datetime.now()
            if(database[account_number]['Amount']>money):
                database[account_number]['Amount']-=money
                transactions[account_number][current_date]=f'Debited {money}(-) available balance {database[account_number]['Amount']}'
                print(f"Amount of INR {money} has been Debited in your account on {date.today()}\n Available Balance={database[account_number]['Amount']}")
            else:
                print("Insufficient balance in your account!!")
        def Deposit(self,account_number):
            current_date=datetime.now()
            money=int(input("Enter amount to be deposited: "))
            database[account_number]['Amount']+=money
            print(f"Amount of INR {money} has been credited in your Bank account {date.today()}\n Available Balance={database[account_number]['Amount']}")
            transactions[account_number][current_date]=f'Credited {money}(+) available balance {database[account_number]['Amount']}'
        def FundTransfer(self,account_number):
            current_date=datetime.now()
            transfer_account=int(input("enter Transfer account number to: "))
            transfer_amount=int(input("Enter amount to be transfered: "))
            if(database[account_number]['Amount']>transfer_amount):
                database[account_number]['Amount']-=transfer_amount
                database[list_accounts[transfer_account]]['Amount']+=transfer_amount
                transactions[account_number][current_date]=f'Debited {transfer_amount}(-) available balance {database[account_number]['Amount']}'
                transactions[transfer_account][current_date]=f'Credited {transfer_amount}(+) available balance {database[account_number]['Amount']}'
                print(f"An amount of INR {transfer_amount} has been transfered to {transfer_account} on {date.today()}")
            else:
                print("Insufficient balance in your account!!")        
        def Transactions(self,account_number):
            for x,y in transactions[account_number].items():
                print(x,y)
            
    print("What do you want ?")
    print(" 1.Create account\n","2.View account details\n","3.Withdraw\n","4.Deposit\n","5.Fund Transfer\n","6.Transactions\n","7.Exit")
    options=int(input())
    obj=BankApplication()
    if(options==1):
        i+=1
        list_accounts.append(obj.createAccount(i))
    elif(options==2):
        print("Accounts list",list_accounts)
        k=int(input("Enter"))
        obj.ViewAccountDetails(list_accounts[k])
    elif(options==3):
        obj.Withdraw(list_accounts[-1])
    elif(options==4):
        obj.Deposit(list_accounts[-1])
    elif(options==5):
        print("Accounts list",list_accounts)
        k=int(input("Enter tranfer account from:"))
        obj.FundTransfer(list_accounts[k])
    elif(options==6):
        print("Accounts list",list_accounts)
        k=int(input("Enter tranfer account"))
        obj.Transactions(list_accounts[k])
    elif(options==7):
        break
    else:
        pass
