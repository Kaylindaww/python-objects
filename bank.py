class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transactionfee=200
        self.loan=0
        self.loan_fees=0.05
        self.loan_limit=3000
    def deposit(self,amount):
        if amount<=0:
            return "Please input a valid amount"
        else:
            self.balance+=amount
            return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"
    def withdraw(self,amount):
        total=self.transactionfee+amount
        if amount<=0:
            return "Cannot withdraw zero or less "
        elif total<amount:
            return "Cannot withdraw you have a less money"
        else:
            self.balance-=total
            return f"Hello {self.name} you have withdrawn {amount} and your balance is {self.balance-(self.transactionfee+amount)} and your transaction fee is {self.transactionfee}"
    def borrow(self,loan):
        5/100*100
        total=self.loan
        if loan<=0:
            return"you can  not borrow a loan"
        elif loan>=0:
            return "you have an outstanding balance"
        else:
            return f"hello {self.name} you can borrow {amount} from us"        
