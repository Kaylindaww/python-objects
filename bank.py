from datetime import datetime as dt
import datetime

class Account:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        self.balance = 0
        self.transaction_fee = 30
        self.loan = 0
        self.loan_limit = 5000
        self.loan_interest = 5 
        self.transactions = []

    def deposit(self,amount):
        if amount<=0:
            return f"please deposit a valid amount"

        else:
            self.balance += amount
            transaction = {"amount":amount,"balance":self.balance,"narration":"You deposited","time":dt.now()}
            self.transactions.append(transaction)
            return f"Hello, {self.name} you have deposited {amount} ,new balance is {self.balance}"
    

     
    def withdraw(self,withdrawal_amount):
        total = withdrawal_amount + self.transaction_fee
        if withdrawal_amount <= 0:
            return "please enter valid amount"

        elif total > self.balance:
            return "Insufficient balance"  

        else:

            self.balance -= total
            transaction = {"amount":withdrawal_amount,"balance":self.balance,"narration":"You withdrew", "time":dt.now()}
            self.transactions.append(transaction)
            return f"Hello {self.name} you have successfully withdrawn {withdrawal_amount} account balance is {self.balance}"

    def borrow(self,loan):
        loan_fees = self.loan_interest * loan / 100
        
        if loan < 0:
            return "Please enter a valid amount"

        elif loan > self.loan_limit:
            return "The amount exeedes the loan limit,please enter a lower amount"

        elif  self.loan > 0:
            return "You have an outstanding loan"

        else:
            repay = loan + loan_fees
            self.loan += repay
            self.balance += loan
            transaction = {"amount":loan,"balance":self.balance,"narration":"You borrowed","time":dt.now()}
            self.transactions.append(transaction)
            return f"You have received a loan of {loan} your account balance now is {self.balance},the amount you will repay is {self.loan}"

    def repay(self,repay_amount):
        if repay_amount < 0:
            return "Please enter a valid amount"

        elif repay_amount < self.loan:
            self.loan = self.loan - repay_amount
            transaction = {"amount":repay_amount,"balance":self.balance,"narration":"You repaid loan","time":dt.now()}
            self.transactions.append(transaction)
            return f"You have repaid {repay_amount} outstanding loan is {self.loan}"

        elif repay_amount > self.loan:
            excess = repay_amount - self.loan
            self.balance += excess
            transaction = {"amount":repay_amount,"balance":self.balance,"narration":"You repaid loan","time":dt.now()}
            self.transactions.append(transaction)
            return f"You have fully settled your loan, account balance is {self.balance}"

    def get_statement(self):
        for transaction in self.transactions:
            amount = transaction["amount"]
            narration = transaction["narration"]
            balance = transaction["balance"]
            time = transaction["time"]
            date = time.strftime("%D")
            print(f"{date}...{narration} {amount}.....Balance {balance}")

            
