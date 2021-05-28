class Bank:
       def __init__(self,account,pin,balance) :
         self.account=account
         self.pin=pin
         self.balance=balance
        
       def withdraw(self):

          return f"I don't remember my {self.pin} for my {self.account} inorder for me to withdraw my {self.balance}"
          
       def deposit(self):

         return f"I am going to check my {self.balance} from {self.account} using my {self.pin}"       
           
