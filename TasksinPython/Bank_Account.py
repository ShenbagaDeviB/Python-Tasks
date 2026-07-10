class bank:
    def __init__(self,account_number,accountholder_name,account_balance):
            self.account_number=account_number;
            self.accountholder_name=accountholder_name;
            self.account_balance=account_balance;
    def deposit(self,amount):
        print("Deposit amount:",amount)
        self.account_balance+=amount;
        print("Account Balance after deposit:",self.account_balance)
    def withdraw(self,amount):
        if amount<=self.account_balance:
            print("Withdrawal amount:",amount)
            self.account_balance-=amount;
            print("Account Balance after withdraw:",self.account_balance)
        else:
            print("Not a proper bank balance")
    def display(self):
        print("Account number:",self.account_number)
        print("Accountholder name:",self.accountholder_name)
        print("Account balance:",self.account_balance)
account_1=bank(1001,"Shen",3000)
account_1.display();
account_1.deposit(2000)
account_1.withdraw(1500)
account_2=bank(1002,"Ren",4000)
account_2.display();
account_2.deposit(3000)
account_2.withdraw(5000)
account_3=bank(1003,"Resh",400)
account_3.display();
account_3.deposit(3000)
account_3.withdraw(5000)
