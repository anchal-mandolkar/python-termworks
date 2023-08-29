def add(D):
    course_code=int(input("Enter the coursecode: "))
    course_name=input("Enter the course name: ")
    faculty=input("Enter the faculty name: ")
    no_of_reg=int(input("Enter the number of registrations done: "))
    D[course_code]=[course_name, faculty, no_of_reg]

def highest_registrations(D):
    high=0
    for i in D:
        if D[i][2]>high:
            high=D[i][2]
    for i in D:
        if high==D[i][2]:
            print(f"The course(s) with highest registrations is: { D[i][0] }")

def display_code(D):
    code=int(input("Enter the course to display: "))
    if code not in D:
        print("Course not found\n")
    else:
        for i in D:
            if i==code:
                print(D[i])

def display(D):
    if D=={}:
        print("Dictionary is empty")
    else:
        for i in D:
            print("Course Code: ", i)
            print("Info: ")
            print(D[i])
            print()

def main():
    D={}
    while True:
        print("1-Add\n2-Highest Registrations\n3-Display Specific\n4-Display All\n5-Exit\n")
        num=int(input("Enter the choice: "))
        if num==1:
            add(D)
        elif num==2:
            highest_registrations(D)
        elif num==3:
            display_code(D)
        elif num==4:
            display(D)
        else:
            exit

if __name__=="__main__":
    main()
