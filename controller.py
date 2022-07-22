from login import Login
from register import Register

# variable
is_exit = False # store stage of this program

# instance of class
L = Login()
R = Register()

while not is_exit:
    operation = input('Register press "1"\nLogin press "2"\nExit program press "3"\n')
    if operation == "1":
        R.register()
    elif operation == "2":
        L.login()
    else:
        is_exit = True
        
print("See you soon :)")
        

