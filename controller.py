from login import Login
from register import Register

# variable
is_finished = False # store stage of this program
is_login = False # store true if user want to register

# instance of class
L = Login()
R = Register()

while not is_login:
    temp = input('Register press "1"\nLogin press "2"\n')
    is_login = (temp == "2")
    if(not is_login):
        R.register()
L.login()

        

