def get_students_info():
    print("="*30)
    students=[]
    length=int(input("Enter the number of students :"))
    print("="*30)
    for studnt in range(length):
        student={}
        total=0
        subjects=[]
        print("-"*30)
        student["Reg.no"]=input("Enter Reg.no(year-dep-reg.no:")
        student["name"]=input("Enter name:")
        subject_list=int(input("Enter number of subjects:"))
        for j in range(subject_list):
            Subject_dict={}
            subject=input("subject name :")
            marks=int(input("Enter marks:"))
            total+=marks
            Subject_dict["Subject"]=subject
            Subject_dict["Marks"]=marks
            if marks>=90:
                Subject_dict["Grade"]="A+"
            elif marks>=80:
                Subject_dict["Grade"]="A-"
            elif marks>=70:
                Subject_dict["Grade"]="B+"
            elif marks>=60:
                Subject_dict["Grade"]="B-"
            elif marks>=55:
                Subject_dict["Grade"]="C"
            elif marks>=50:
                Subject_dict["Grade"]="D"
            else:
                Subject_dict["Grade"]="F"
            
            subjects.append(Subject_dict)
        
        student["Total"]=total
        student["Subjects"]=subjects
        average=total/len(student["Subjects"])
        student["Average"]=average
        students.append(student)
        print("-"*30)
    return students
def save_student_info(student_list):
    file=open("student.txt","a")
    for student in student_list:
        file.write("==========================\n")
        file.write("Reg.no:"+student["Reg.no"]+"\n")
        file.write("Name :"+student["name"]+"\n")
        for subject in student["Subjects"]:
            file.write("Subject:"+subject["Subject"]+"\n")
            file.write("Mark :"+str(subject["Marks"])+"\n")
            file.write("Grade:"+subject["Grade"]+"\n")
            file.write("\n")
        file.write("Total:"+str(student["Total"])+"\n")
        file.write("Average:"+str(student["Average"])+"\n")
        file.write("==========================\n")
    file.close()
def search_student():
    reg_no=input("Enter Reg.no:")
    file=open("student.txt","r")
    found=False
    for line in file:
        if reg_no in line:
            found=True
        if found==True:
            print(line,end="")
            if line.startswith("=========================="):
                break
    if found==False:
        print("<--------Record not found--------->")
    file.close()
def display_students_info():
    found=False
    file=open("student.txt","r")
    data=file.read()
    print(data,end="")
    file.close()
def delete_student():
    import os
    reg_no = input("Enter Reg.no: ")
    file = open("student.txt", "r")
    temp = open("temp.txt", "w")
    found = False
    skip = False
    for line in file:
        if line.strip() == "Reg.no:" + reg_no:
            found = True
            skip = True
            continue
        if skip:
            if line.startswith("=========================="):
                skip = False
            continue
        temp.write(line)
    file.close()
    temp.close()
    os.remove("student.txt")
    os.rename("temp.txt", "student.txt")
    if found == True:
        print("Student deleted successfully.")
    else:
        print("Record not found.")
def update_student():
    import os
    reg_no = input("Enter Reg.no to update: ")
    file = open("student.txt", "r")
    temp = open("temp.txt", "w")
    found = False
    for line in file:
        if line.strip() == "Reg.no:" + reg_no:
            found = True
            while True:
                next_line = next(file)
                if next_line.startswith("=========================="):
                    break
            temp.write("=========================\n")
            reg_no=input("Reg.no(yyyy-Dep-Reg.no):")
            name = input("Enter New Name: ")
            temp.write("Name :" + name + "\n")
            subject_count = int(input("Enter number of subjects: "))
            total = 0
            for i in range(subject_count):
                subject = input("Subject: ")
                marks = int(input("Marks: "))
                total += marks
                if marks >= 90:
                    grade = "A+"
                elif marks >= 80:
                    grade = "A-"
                elif marks >= 70:
                    grade = "B+"
                elif marks >= 60:
                    grade = "B-"
                elif marks >= 55:
                    grade = "C"
                elif marks >= 50:
                    grade = "D"
                else:
                    grade = "F"
                temp.write("Reg.no:" + reg_no + "\n")
                temp.write("Subject:" + subject + "\n")
                temp.write("Mark :" + str(marks) + "\n")
                temp.write("Grade:" + grade + "\n\n")

            average = total / subject_count

            temp.write("Total:" + str(total) + "\n")
            temp.write("Average:" + str(average) + "\n")
            temp.write("==========================\n")

        else:
            temp.write(line)

    file.close()
    temp.close()

    os.remove("student.txt")
    os.rename("temp.txt", "student.txt")

    if found:
        print("Student updated successfully.")
    else:
        print("Reg.no not found.")


def login():
    password="admin1234"
    i=0
    attempts=3
    print("="*30)
    while attempts>0:
        search=input("Enter password:")
        if password==search:
            print("<------Accessed------>")
            return True
        else:
            attempts-=i+1
            print(f"<------{attempts} attempts reamining------>")
        print("="*30)
def menu():
    print("="*20)
    print("1.Add Student")
    print("2.display students")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.exit")
    print("="*20)
    
def main():
    while True:
        menu()
        choice=int(input("Enter choice :"))
        if choice==1:
            result=get_students_info()
            save_student_info(result)
        if choice==2:
            display_students_info()
        if choice==3:
            search_student()
        if choice==4:
            update_student()
        if choice==5:
            delete_student()
        if choice==6:
            print("<-----'working terminated'----->")
            break
if login():
    main()
else:
    print("<------Acess denied------>")
