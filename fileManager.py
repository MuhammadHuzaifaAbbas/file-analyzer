import os
import hashlib
class CurrentDirectory:
    def current_directory(self):
        path= os.getcwd()
        return path
        print(path)
class Login:
    def set_password(self):
        if Login():
            self.password=input("Enter New password:")
            with open("password.txt","w") as file:
                file.write(self.password)
        else:
            print("----------Access Denied-------------")
    def login(self):
        attempts=3
        while attempts>0:
            self.verifying_password=input("Enter Password :")
            with open("password.txt","r") as file:
                data=file.read()
                attempts-=1
                if data==self.verifying_password:
                    print("===========Access Granted===========")
                    break
                else:
                    print(f"-------{attempts} Attempts Remains--------")
class ListDirectory(CurrentDirectory,Login):
    def show_items(self):
        path=self.current_directory()
        for items in os.listdir(path):
            print(items)
    def specific_folder(self):
        self.location=input("Enter location")
        self.folder=input("Enter folder name:")
        self.found_folder_location=rf"C:\Users\CANTTBOARD1\{self.location}\{self.folder}"
        self.found_folder=rf"C:\Users\CANTTBOARD1\{self.folder}"
        if os.path.exists(self.found_folder):
            for items in os.listdir(self.found_folder):
                print("^^^^^^^^^^^^^^^^^^^^^^^^^")
                print(items)
        elif os.path.exists(self.found_folder_location):
            print("-"*40)
            for root,folders,files in os.walk(self.found_folder_location):
                for file in files:
                    print(file)
                print("-"*40)

        else:
            print("<=============Folder doest exist==============> ")
    def direct_folder(self):
        count=0
        self.folder=input("Enter folder name:")
        self.found_folder=rf"C:\Users\CANTTBOARD1\{self.folder}"
        self.extension_path=os.path.join(os.path.expanduser("~"),self.folder)
        if os.path.exists(self.found_folder):
            for items in os.listdir(self.found_folder):
                print("-"*40)
                count+=1
                print(items)
        if os.path.exists(self.extension_path):
            extension_count={}
            for root,folders,files in os.walk(self.extension_path):
                for file in files:
                    name,extension=os.path.splitext(file)
                    if extension in extension_count:
                        extension_count[extension]+=1
                    else:
                        extension_count[extension]=1
        print("Total files:",count)
        report=extension_count
        self.file_extension_print(report)
    def whole_drive_scan(self):
        def handle_error(error):
            print(f"[permission error] {error}")
        paths=[
            os.path.join(os.path.expanduser("~"), "Desktop"),
            os.path.join(os.path.expanduser("~"), "Downloads"),
            os.path.join(os.path.expanduser("~"), "Documents"),
            os.path.join(os.path.expanduser("~"), "Pictures"),
            os.path.join(os.path.expanduser("~"), "Videos")
]
        total_folder=0
        total_files=0
        for path in paths:
            for root,folders,files in os.walk(path,onerror=handle_error):
                total_files+=len(files)
                total_folder+=len(folders)
        empty_folder=0
        for path in paths:
            for root,folders, files in os.walk(path,handle_error):
                if len(folders)==0 and len(files)==0:
                    empty_folder+=1
                    print(root)
        dublicate_count=0
        hash_dict={}
        for path in paths:
            for root,folders,files in os.walk(path,handle_error):
                for file in files:
                    file_path=os.path.join(root,file)
                    with open(file_path,"rb") as f :
                        print("File Opened:",file_path)
                        file_hash=hashlib.md5(f.read()).hexdigest()
                        print("Hash Created :",file_path)
                    if file_path in hash_dict:
                        dublicate_count+=1
                    else:
                        hash_dict[file_hash]=file_path
                    print(file_path)
        print("="*40)
        print("        Drive Scan Report")
        print("="*40)
        print("Total folders:",total_folder)
        print("Total files:",total_files)
        print("Empty folder:",empty_folder)
        print("Dublicate files:",dublicate_count)
        print("="*40)
    def file_extensions_report(self):
        paths=[
                    os.path.join(os.path.expanduser("~"), "Desktop"),
                    os.path.join(os.path.expanduser("~"), "Downloads"),
                    os.path.join(os.path.expanduser("~"), "Documents"),
                    os.path.join(os.path.expanduser("~"), "Pictures"),
                    os.path.join(os.path.expanduser("~"), "Videos")
        ]
        extension_count={}
        for path in paths:
            for root,folders,files in os.walk(path):
                for file in files:
                    name,extension=os.path.splitext(file)
                    if extension in extension_count:
                        extension_count[extension]+=1
                    else:
                        extension_count[extension]=1
        report=extension_count
        self.file_extension_print(report)
    def file_extension_print(self,report_extension_dict):
        count_extensions=0
        print("="*40)
        print("         File Extensions report")
        print("="*40)
        for extension,count in report_extension_dict.items():
            print("->",extension,":",count)
            count_extensions+=1
        print("-"*40)
        print("Total Extensions:",count_extensions)
        print("-"*40)
    def pause(self):
        input("Press Enter to continue :")
        

def clear_screen():
    os.system("cls")


def main():
    obj=ListDirectory()
    while True:
        print("===========================")
        print("       1.Login")
        print("===========================")
        try:
            option=int(input("Enter your choice :"))
        except ValueError as e:
            print(e)
        if option==1:
            obj.login()
            while True:
                print("=====================================")
                print("            Menu")
                print("=====================================")
                print("2.View current directory")
                print("3.Files of current directory")
                print("4.View fies of specific Location")
                print("5.View directory except specific location ")
                print("6.Scan C drive")
                print("7.File Extension Report")
                print("=====================================")
                print("*************************************")
                try:
                    choice=int(input("Enter your choice :"))
                except ValueError as e:
                    print(e)
                print("*************************************")
                if choice==2:
                    clear_screen()
                    obj.current_directory()
                    obj.pause()
                elif choice==3:
                    clear_screen()
                    obj.show_items()
                    obj.pause()
                elif choice==4:
                    clear_screen()
                    obj.specific_folder()
                    obj.pause()
                elif choice==5:
                    clear_screen()
                    obj.direct_folder()
                    obj.pause()
                elif choice==6:
                    clear_screen()
                    obj.whole_drive_scan()
                    obj.pause()
                elif choice==7:
                    clear_screen()
                    obj.file_extensions_report()
                    obj.pause
                elif choice==0:
                    print("="*40)
                    print("        Progrsm Terminated")
                    print("="*40)
                    break
main()