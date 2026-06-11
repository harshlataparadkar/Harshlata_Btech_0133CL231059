class AccountLockedError(Exception):
    pass
class LoginSystem:
    __password = "python@123"
    __attempts = 3
    def login(self,password):
        try:
            if self.__attempts == 0:
                raise AccountLockedError("account locked")
            
            if password == self.__password:
                print("Login successful")

            else:
                self.__attempts -= 1
                print("wrong password")
                print("Remaining password",self.__attempts)
                
                if self.__attempts == 0:
                    raise AccountLockedError("account locked")
        except AccountLockedError as e:
            print(e)
            
obj = LoginSystem()
for i in range(4):
    pwd = input("Enter password:")
    obj.login(pwd)