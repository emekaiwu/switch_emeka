
class Banking():
    balance = 0.0
    def __init__(self,username,phone,email):
        self.username = username
        self.phone = phone
        self.email = email
        self.acc_no = ""
    def create_Account(self):
        self.acc_no = ""
        print (input("enter your account number"))

    def check_Balance(self,acc_no):
        return self.balance

    def deposit(self,amount):
        self.balance+= amount

        return self.balance
    def withdraw(self,amount):
        if self.balance < amount:
            print ("insufficient balance")

        else:
            self.balance-=amount
            print("you have withdrawn",amount,"and your balance is",self.balance)
        return self.balance
cost_obj = Banking("frank","080633391178","emeka@gmail.com")
acc_no = cost_obj.create_Account()
print (cost_obj.check_Balance(acc_no))
cost_obj.withdraw(25000)
cost_obj.deposit(50000)
cost_obj.withdraw(15000)
 
