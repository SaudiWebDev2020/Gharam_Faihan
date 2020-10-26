class user:
    def __init__(self, name, email_address ,account_balance):
        self.name = name		
        self.email = email_address		
        self.account_balance = account_balance

def make_withdrawal(self, amount):
    self.account_balance=self.account_balance-amount
    return self.account_balance

def make_deposits(self, amount):
    self.account_balance=self.account_balance+amount
    return self.account_balance

def display_user_balance(self):
    print ("user ", self.name , "Balance: $", self.account_balance)


def transfer(from_account, to_account, amount):
        from_account.account_balance = (make_withdrawal(from_account,amount))
        to_account.account_balance = (make_deposits(to_account,amount)) 



user1 = user("John", "John@gmail.com" , 800)
user2 = user("tony", "tony12@gmail.com" ,3000 )
user3 = user("sara", "sara22@gmail.com" ,1000 )

user1.account_balance = make_deposits(user1, 300)
user1.account_balance = make_deposits(user1, 100)
user1.account_balance = make_deposits(user1, 50)
user1.account_balance = make_withdrawal(user1, 400)
display_user_balance(user1)
#output = user  John Balance: $ 850

user2.account_balance = make_deposits(user2 , 200)
user2.account_balance = make_deposits(user2 , 1000)
user2.account_balance = make_withdrawal(user2, 1000)
user2.account_balance = make_withdrawal(user2, 100)
display_user_balance(user2)
#user  tony Balance: $ 3100

user3.account_balance=make_deposits(user3 , 1000)
user3.account_balance=make_withdrawal(user3 , 1500)
user3.account_balance=make_withdrawal(user3 , 500)
display_user_balance(user3)

#user  sara Balance: $ 0

transfer(user2 , user3 , 1000 )
display_user_balance(user2)
display_user_balance(user3)

#user  tony Balance: $ 2100
#user  sara Balance: $ 1000