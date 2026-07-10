class BankAccount:
    def __init__(self,acc_no,name):
        self.acc_no=acc_no
        self.name=name
        self.__balance=0
        self.transaction_history=[]
    def information_account(self):
        print(f"Account Holder name:{self.name}|Account Number:{self.acc_no}|Balance:{self.__balance}")
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f'Account Holder Name:{self.name} |Amount deposited:{amount}')
            self.transaction_history.append(f"Deposited amount:{amount}")
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            print(f'Account Holder Name:{self.name} |Amount withdraw:{amount}')
            self.transaction_history.append(f"Amount withdraw:{amount}")
            return
        print("Insufficient funds")
    def check_balance(self):
        if self.__balance>=0:
            print(f"Balance amount:{self.__balance}")
            return
        print("Insufficient balance")
    def show_transaction_history(self):
        print("Transaction History")
        for transaction in self.transaction_history:
            print(transaction)
    def transfer_money(self,other_account,amount):     
        if self.__balance>=amount:
            self.__balance-=amount
            other_account.__balance+=amount
            self.transaction_history.append(f"{self.name} sending amount:{amount}to {other_account.name}")
            other_account.transaction_history.append(f"{other_account.name} Received amount: {amount} from {self.name}")
            print(f"{self.name} transfered {amount} to {other_account.name}")
        else:
            print("Insufficient amount")
    def get_balance(self):
        return self.__balance
    def reduce_balance(self,amount):
        self.__balance-=amount



acc1=BankAccount(1,"Yashaswini M")
acc2=BankAccount(2,"Yukta")

acc1.information_account()
acc2.information_account()

acc1.deposit(1000)
acc2.deposit(500)

acc1.withdraw(500)
acc2.withdraw(500)

acc1.check_balance()
acc2.check_balance()

acc1.transfer_money(acc2,200)
acc2.deposit(1000)
acc2.transfer_money(acc1,300)

acc1.show_transaction_history()
acc2.show_transaction_history()

class SavingsAccount(BankAccount):
    def __init__(self,acc_no,name,interest_rate):
        super().__init__(acc_no,name)
        self.interest_rate= interest_rate 
    def information_saving(self):
        print(f"Account no:{self.acc_no} |Account Holder:{self.name} |Interest rate:{self.interest_rate}")
    def add_interest(self):
        balance=self.get_balance()
        if balance>0:
            interest_amount=balance*(self.interest_rate/100)
            self.deposit(interest_amount)
        else:
            print("NO balance available to return interest")

saving1=SavingsAccount(3,"Yamini",5)
saving1.add_interest()

class CurrentAccount(BankAccount):
    def __init__(self,acc_no,name,overdraft_limit):
        super().__init__(acc_no,name)
        self.overdraft_limit=overdraft_limit
    def information_current(self):
        print(f"Account no:{self.acc_no} |Account Holder:{self.name} |Overdraft limit:{self.overdraft_limit}")
    def withdraw(self,amount):
        balance=self.get_balance()
        available=balance+self.overdraft_limit
        if amount<=available:
            print(f"withdrawal allowed :{amount}")
            self.reduce_balance(amount)
            self.transaction_history.append(f"Amount {amount} withdrawed in currrent account")
        else:
            print("Withdrawal rejected")
    def check_balance(self):
        print(f"Curent balance amount:{self.get_balance()}")
current1=CurrentAccount(1,"Yashaswini M",5000)
current1.withdraw(5000)
current1.check_balance()

class Bank:
    def __init__(self):
        self.accounts=[]
    def add_account(self,account):
        self.accounts.append(account)
    def display_account(self):
        if len(self.accounts)==0:
            print("No Account Found")
            return
        else:
            for account in self.accounts:
                account.information_account()
            
        
    def search_account(self,account_number):
        for account in self.accounts:
            if account.acc_no==account_number:
                print("Account Found!!")
                account.information_account()
                return
        print("Account Not Found")
    def delete_account(self,account_number):
        for account in self.accounts:
            if account.acc_no==account_number:
                self.accounts.remove(account)
                print("Account Deleted Successfully")
                return
        print("Account Not Found")
    def update_account(self,acc_no,name):
        for account in self.accounts:
            if account.acc_no==acc_no:
                account.name=name
                print("Account Updated Successully!")
                account.information_account()
                return
        print("Account Not Found")
        def transfer_money(self, sender_acc_no, receiver_acc_no, amount):
            sender = None
            receiver = None
            for account in self.accounts:
                if account.acc_no == sender_acc_no:
                    sender = account
                    break
            for account in self.accounts:
                if account.acc_no == receiver_acc_no:
                    receiver = account
                    break
            if sender is None:
                print("Sender account not found.")
                return
            if receiver is None:
                print("Receiver account not found.")
                return
            if sender_acc_no == receiver_acc_no:
                print("Cannot transfer money to the same account.")
                return
            if amount <= 0:
                print("Invalid amount.")
                return
            if sender.get_balance() < amount:
                print("Insufficient balance.")
                return
            sender.withdraw(amount)
            receiver.deposit(amount)

            print(f"₹{amount} transferred successfully.")
            print(f"From Account : {sender.name}")
            print(f"To Account   : {receiver.name}")
acc5=BankAccount(5,"Meena")
acc6=BankAccount(6,"Amulya")
acc7=BankAccount(7,"Pavithra")
bank1=Bank()
bank1.add_account(acc5)
bank1.add_account(acc6)
bank1.add_account(acc7)

bank1.display_account()
bank1.search_account(5)
bank1.delete_account(7)
bank1.update_account(7,"Rahul")



