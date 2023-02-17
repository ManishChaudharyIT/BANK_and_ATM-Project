#which type data should be use in atm
'''
Pin
Balance
what we can do using atm machine 
pin generate
pn change
check balance
widhdraw
'''
'''constructor baisc mean a function in side the class
which is look like :: def __init__(self):
it automatically execute  mean when we create class object it automatically call mtlb ki consturtor ke ander ka code automaticalsly execute
 ho jata hai
NOte::it is a special function because it has super power mean whitin which code is writen within function no need to call like we call 
in function
like magic JITNI bar object banega utni baar constructor execute hoga
@ class are two types 1.buildin classes(like list/int/tuple/set) 2. user defined classes
'''
class ATM:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
        
    def menu(self):
        user_input=input(''' Hi can I help You
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit ............''')

        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.chaange_pin()
        elif user_input =='3':
            self.check_balance()
        elif user_input=='4':
            self.withdraw()
        else:
            exit()
    def create_pin(self):
        user_pin=input('Enter your pin')
        self.pin=user_pin
        user_balanec=int(input('Enter balance'))
        self.balance=user_balanec
        print('Pin created successfully::')
        self.menu()
    def chaange_pin(self):
        old_pin=input('Enter your old pin')
        if old_pin==self.pin:
        #let him change pin
            new_pin=input('Enter new pin..')
            self.pin=new_pin
            print("Pin change pin successfull..")
        else:
            print('You entered wrong pin ')
            self.menu()
    def check_balance(self):
        user_pin=input('enter your pin')
        if user_pin==self.pin:
            print('Your balance is ',self.balance)
        else:
            print("Sorry you entered wrong input")
            self.menu()
    def withdraw(self):
        user_pin=input('Enter your pin..')
        if user_pin==self.pin:
            amount=int(input("enter your ammount.."))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print("withdraw successfull..")
                print('Available balance is ...',self.balance)
            else:
                print("Insufficent Balance..")
                
        else:
            print("Your pin is incorrect")
        self.menu()
obj=ATM()
obj.create_pin()
obj.chaange_pin()
obj.check_balance()
obj.withdraw()


