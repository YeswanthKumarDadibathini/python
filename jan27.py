'''class student:
    pass
student1=student()
class student:
    name="Yeshu"
    age=20
    cgp=7.2
student1=student()
print(student1.name)
print(student1.cgp) 


class student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage

    def student_del(self):
        print(f"{self.name} is in the class {self.grade} with {self.percentage}")
student1=student("Yeswanth",10,98)
student2=student("Manju",10,98)

student1.student_del()
student2.student_del()


class bank:
    def __init__(self,bankACC,branch,withdraw):
        self.bankACC=bankACC
        self.branch=branch
        self.withdraw=withdraw
    def bankdet(self):
        print(f"The bank account number {self.bankACC} and branch name {self.branch} amount to withdraw {self.withdraw}")

details=bank(123456789,"Kadapa",10000)
details.bankdet()
'''

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def multi(self):
        return self.num1*self.num2

a=int(input("Enetr the number: "))
b=int(input("Enter the second number: "))

total=calculator(a,b)
 
print("add",total.add())
print("sub",total.sub())
print("mul",total.multi())


    
        
