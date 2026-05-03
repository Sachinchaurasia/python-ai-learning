students=[ ]

#add students

def add_student():
    name=input("enter name:")
    marks=int(input("enter marks:"))
    students.append({
        "name":name,
        "marks": marks})
    
#display students
def view_student():
    for s in students:
        print(s)
        
#search students

def search_student():
    name=input("enter name")
    for s in students:
        if s["name"]==name:
            print(s)
#update students

def update_student():
    name=input("enter name")
    for s in students:
        if s["name"]==name:
            s["marks"]=int(input("enter  marks"))
#delete students

def delete_student():
    name=input("enter name")
    for s in students:
        if s["name"]==name:
            students.remove(s)
#menu

while True:
    print("1. add students 2.view students 3. search students 4. update students 5. delete students 6. exit")
    
    choice=int(input("enter choice:"))
    
    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        search_student()
    elif choice==4:
        update_student()
    elif choice==5:
        delete_student()
    elif choice==6:
        break
    else:
        print("invalid choice")
        
        