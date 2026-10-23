class Login:
    def login_system(self):
        attempts=3
        while attempts>3:
            print("//////////////////////////////////////////")
            self.password=input("-....Enter Password....-")
            print("//////////////////////////////////////////")
            with open("password.txt","r") as file:
                data=file.read()
                if self.password==data:
                    print("<<<<<<<<<<< Login Successful >>>>>>>>>>>")
                    return True
                else:
                    attempts=attempts-1
                    print(f"====={attempts} Attempts Remaining=====")
                    print("==================Acess Denied===============")
                    return False
    def reset_password(self):
        print("//////////////////////////////////////////")
        self.previous_password=input("-....Enter Password....-")
        print("//////////////////////////////////////////")
        with open("password.txt","r") as file:
            data=file.read()
            if self.previous_password==data:
                print("<<<<<<<<<<< Login Successful >>>>>>>>>>>")
                self.new_password=input("-.... Enter New Password....-")
                with open("password.txt","w") as file:
                    file.write(self.new_password)
                    return True
            else:
                print("==================Acess Denied===============")
                

            




