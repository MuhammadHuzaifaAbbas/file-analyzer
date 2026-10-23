class Login:
    def set_password(self):
        print("===================================")
        self.password=input("->Enter Password :")
        with open("password.txt","w")as file:
            file.write(self.password)
        print("===================================")
    def login(self):
        attempts=3
        while attempts>0:
            print("===================================")
            password=input("->Enter password:")
            print("===================================")
            with open("password.txt","r") as file:
                data=file.read()
            if password == data:
                print("<------Login successful------>")
                print("===================================")
                return True
            else:
                attempts=attempts-1
                print(f"====={attempts} Attempts Remaining=====")
        print("==================Acess Denied===============")
        return False
    def reset_password(self):
        print("===================================")
        previous_password=input("->Enter Current Password :")
        print("===================================")
        with open("password.txt","r") as file:
            data=file.read()
            if previous_password == data:
                with open("password.txt","w")as file:
                    print("===================================")
                    self.password=input("->Enter New Password :")
                    file.write(self.password)
                    print("===================================")
            else:
                print("======Acess denied===========")
    def  Logout(self):
        print("=========Logout Successfully============")

def number_input():
    while True:
        try:
            count=int(input("Enter number of tasks :"))
            return count
        except ValueError as e:
            print(e)
class TaskManager(Login):
        def __init__(self):
            self.tasks=[]
        def get_next_id(self):
            try:
                last_id = 0
                with open("taskmanager.txt", "r") as file:
                    for line in file:
                        if line.startswith("*Id:"):
                            last_id = int(line.split(":")[1])
                return last_id + 1
            except FileNotFoundError:
                return 1
        def add_task(self):
            from datetime import datetime
            for i in range(number_input()):
                task={}
                task["id"]=self.get_next_id()
                task["title"]=input("Enter Title :")
                task["description"]=input("Enter Description :")
                task["priority"]=input("Enter priority(low/medium/high):")
                task["status"]=input("Enter Status (pending/completed) :").lower()
                current_datetime= datetime.now().strftime("%d-%m-%Y %I:%M:%S %p ")
                task["Created at"]=current_datetime
                self.tasks.append(task)
            self.save_tasks()
            self.tasks.clear()
        def save_tasks(self):
            for task in self.tasks:
                with open("taskmanager.txt","a") as file:
                    file.write("*Id:"+str(task["id"])+"\n")
                    file.write("*Title:"+task["title"]+"\n")
                    file.write("*Description:"+task["description"]+"\n")
                    file.write("*Priority:"+task["priority"]+"\n")
                    file.write("*status:"+task["status"]+"\n")
                    file.write("*Created at:"+task["Created at"]+"\n")
                    file.write("<=========================>\n")
        def view_tasks(self):
            with open("taskmanager.txt","r") as file:
                for line in file:
                    print(line,end="")

        def view_pending_tasks(self):
            with open("taskmanager.txt", "r") as file:
                block = ""
                for line in file:
                    block += line
                    if line.strip() =="<=========================>":
                        if "*status:pending" in block.lower():
                            print(block)
                        block = ""
        def view_complete_tasks(self):
            with open("taskmanager.txt", "r") as file:
                block = ""
                for line in file:
                    block += line
                    if line.strip() == "<=========================>":
                        if "*status:complete" in block.lower():
                            print(block)
                        block = ""
        def search_task(self):
            id_to_find=number_input()
            found=False
            with open("taskmanager.txt","r") as file:
                for line in file:
                    if line.strip()=="*Id:"+str(id_to_find):
                        found=True
                    if found==True:
                        print(line,end="")
                    if line.strip()=="<=========================>":
                        break
            if found==False:
                        print("<---------Id not found---------->")
        def delete_task(self):
            if self.login()==True:
                import os
                id_to_find=number_input()
                found=False
                skip=False
                file=open("taskmanager.txt","r")
                temp=open("temptaskmanager.txt","w")
                for line in file:
                    if line.strip()=="*Id:"+str(id_to_find):
                        found=True
                        skip=True
                        continue
                    if skip==True:
                        if line.strip()=="<=========================>":
                            skip=False
                            continue
                    temp.write(line)
                file.close()
                temp.close()
                os.remove("taskmanager.txt")
                os.rename("temptaskmanager.txt","taskmanager.txt")
                if found==True:
                    print("========Task Deleted Successfully=======")
                else:
                    print("=============Task not Found=================")
            else:
                print("=============Acess Denied============")
        def update_task(self):
            if self.login()==True:
                import os
                found=False
                skip=False
                id_to_find=number_input()
                with open("taskmanager.txt","r")as file,open("temptaskmanager.txt","w") as temp:
                    for line in file:
                        if line.strip()=="*Id:"+str(id_to_find):
                            found=True
                            skip=True

                            new_task=input("->Enter updated task:")
                            new_description=input("->Enter new description:")
                            new_priority=input("Enter new priority(low/medium/high):")
                            new_status=input("->Enter new status(pending/complete):")
                            temp.write("Id:"+str(id_to_find)+"\n")
                            temp.write("Title:"+new_task+"\n")
                            temp.write("Description:"+new_description+"\n")
                            temp.write("Priority:"+new_priority+"\n")
                            temp.write("Status:"+new_status+"\n")
                            temp.write("<=========================>\n")
                            continue
                        if skip:
                            if line.strip()=="<=========================>":
                                skip=False
                            continue
                        else:
                            temp.write(line)
                if found: 
                    os.remove("taskmanager.txt")
                    os.rename("temptaskmanager.txt","taskmanager.txt")
                    print("===========Record updated successfully===========")    
                else:
                    os.remove("temptaskmanager.txt")
                    print("===========Record not found============")
            else:
                return
        def delete_all_tasks(self):
            if self.login():
                open("taskmanager.txt", "w").close()
                print("====== All Tasks Deleted Successfully ======")

def main():
    import os
    task=TaskManager()
    while True:
        print("1.Login")
        option=number_input()
        if option==1:
            task.login()
            while True:
                print("====================TASK MANAGER====================")
                print("2.Set Password")
                print("3.Add Task")
                print("4.View Task")
                print("5.View Pending Task")
                print("6.View Completed Task")
                print("7.Update Task")
                print("8.Delete Task")
                print("9.Reset Password")
                print("10.Logout")
                print("11.Delete file data")
                print("12.Screen ")
                print("0.Exit")
                print("=====================================================")
                choice=number_input()
                if choice==2:
                    task.set_password()
                elif choice==3:
                    task.add_task()
                elif choice==4:
                    task.view_tasks()
                elif choice==5:
                    task.view_pending_tasks()
                elif choice==6:
                    task.view_complete_tasks()
                elif choice==7:
                    task.update_task()
                elif choice==8:
                    task.delete_task()
                elif choice==9:
                    task.reset_password()
                elif choice==10:
                    task.Logout()
                elif choice==11:
                    task.delete_all_tasks()
                elif choice==12:
                    os.system("cls")
                elif choice==0:
                    break
                else:
                        print("<----------Invalid Choice<----------")
main()





                    


