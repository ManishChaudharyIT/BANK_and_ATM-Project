class Bank:
    def __init__(self):
        self.acc_No='100'
        self.adhar_no=''
        self.mobile=''
        self.balance=0
        self.menu()
    def menu(self):
        print("*"*80 )
        print("                                 Wel Come in SBI" )
        print("*"*80)
        print()
        user_input=input(''' How May  I help You:..
        1. Press 1 for  New Account::
        2. Press 2 for  Deposit::
        3. Press 3 for  Withdraw:: 
        4. Press 4 for  Check Balance::
        5. Press 5 for  Customer Details::
        6. Press 6 for  exit::''')
        print()

        if user_input==1:
            self.create_account()
        elif user_input==2:
            self.deposit_ammount
        elif user_input==3:
            self.withdraw_amount()
        elif user_input==5:
            self.customer_details()
        else:
            exit()

    def create_account(self):
        user_adhar=input('Enter your Adhar number>')
        self.acc_No=user_adhar
        user_mobile=input("Enter your Mobile number>")
        self.mobile=user_mobile
        amount=int(input("Enter first time intial amount "))
        self.balance=amount
        print("Account opening successfully...")
        self.menu()
    def deposit_ammount(self):
        user_input=input("Enter your Adhar or Account number")
        if user_input==self.acc_No or user_input==self.adhar_no:
            user_amount=int(input("Enter your deposit ammount"))
            self.balance=self.balance+user_amount
            print()
            print()
            print("Transaction Completed ",self.balance)
        else:
            print("You entered wrong adhary/account number")
        
    def withdraw_amount(self):
        user_input=input("Enter your Account or Adhar number")
        if user_input==self.acc_No or user_input==self.adhar_no:
            user_amount=int(input("Enter your amount"))
            if self.balance>=user_amount:
                self.balance=self.balance-user_amount
                print()
                print()
                print("Transaction completed...")
                print("Availabel Balance is......",self.balance)
    def check_balance(self):
        user_input=input("Enter your Adhar or account numbe")
        if  user_input==self.acc_No or user_input==self.adhar_no:
            print("Current balance Is....",self.balance)
        else:
            print("wrong input")
    def customer_details(self):
        user_input=input("Please enter your Adhar/Account number")
        if user_input==self.acc_No or user_input==self.adhar_no:
            print("Customer Details ..........\n","Account number Is...>>>",self.acc_No,"\n Adhar number Is...>>>",self.adhar_no,"\n Current Balance Is..>>>>",self.balance,"\n Mobile number....>>>",self.mobile)
        else:
            print("Given data not matched...")
    def exit(self):
        pass

obj=Bank()
obj.create_account()
#obj.withdraw_amount()
#obj.deposit_ammount()
#obj.check_balance()
#obj.customer_details()

