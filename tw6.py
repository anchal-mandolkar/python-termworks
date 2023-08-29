class Person:
    def __init__(self,fname="",lname="",email=""):
        self.fname=fname
        self.lname=lname
        self.email=email
    def getFullname(self):
        return self.fname +" "+ self.lname

class Customer(Person):
    def __init__(self,fname,lname,email,cust_id):
        Person.__init__(self,fname,lname,email)
        self.cust_id=cust_id
    def getCust_id(self):
        return self.cust_id

class Employee(Person):
    def __init__(self,fname,lname,email,PAN):
        Person.__init__(self,fname,lname,email)
        self.PAN=PAN
    def get_PANno(self):
        return self.PAN
    
def display(obj):
    if isinstance(obj, Customer):
        print("Customer details")
        print("Customer Full name",obj.getFullname())
        print("Customer ID",obj.getCust_id())
    else :
        print("Employee details")
        print("Employee full name: ",obj.getFullname())
        print("Employeee PAN: ",obj.get_PANno())
    
def main():
    Cust_obj=Customer("Anchal","Mandolkar","anchal123@gmail.com",120)
    EMP_obj=Employee("Monu","Mandolkar","monu345@gmail",21)
    display(Cust_obj)
    display(EMP_obj)
    
if __name__=='__main__':
    main()