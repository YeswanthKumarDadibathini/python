#lambda functions

# def sq(x):
#     return x**2
# print(sq(5))

# y=lambda x:x**2
# print(y(5))

# x=10
# y=20
# z=lambda a:(x+y)
# print(z(0))

# a=int(input("a: "))
# b=int(input("b: "))
# c=lambda a,b:a if(a>b) else b
# print(c(a,b))

# list1=[1,2,3,4,5,6]
# z=list(map(lambda x:x**2,list1))
# print(z)

# class bank:
#     def __init__(self,bankACC,branch,withdraw,balance):
#         self.bankACC=bankACC
#         self.branch=branch
#         self.withdraw=withdraw
#         self.__balance=balance
#     def bankdet(self):
#         print(f"The bank account number {self.bankACC} and branch name {self.branch} amount to withdraw {self.withdraw} the remainind balance {self.__balance} ")

#     def get_balance(self):
#         return self.__balance 

# details=bank(123456789,"Kadapa",10000,90000)
# details.bankdet()

# class cars:
#     def __init__(self,car_model,owner_name,branch,carplate):
#         self.car_model=car_model
#         self.owner_name=owner_name
#         self.branch=branch
#         self.__carplate=carplate
#     def car_del(self):
#         print(f"model of the car {self.car_model} owners name {self.owner_name} location of the branch {self.branch} and car plate {self.__carplate} ")
    
#     def get_plate(self):
#         return self.__carplate

# detailss=cars('BMW','yeshu','kadapa',1)
# detailss.car_del()

# class student:
#     def __init__(self,name,grade,percentage):
#         self.name=name
#         self.grade=grade
#         self.percentage=percentage
#     def student_call(self):
#         print(f"Name of the student {self.name} grade {self.grade} percentage {self.percentage} ")

# d=student("Yeshu","Btech",7.2)

# class update(student):
#     def __init__(self,name,grade,percentage,branch):
#         super().__init__(name,grade,percentage)
#         self.branch=branch
    
#     def update_call(self):
#         print(f"Name of the student {self.name} grade {self.grade} percentage {self.percentage} and branch {self.branch}")
    
# de=update("Yeshu","Btech",7.2,"CSE")
# de.update_call()

# class student:
#     def __init__(self,Name,regno,branch):
#         self.Name=Name
#         self.regno=regno
#         self.branch=branch
    
# class mentor(student):
#     def __init__(self,Name,regno,branch,mentorname):
#         super().__init__(Name,regno,branch)
#         self.mentorname=mentorname
    
#     def mentor_call(self):
#         print(f"Name of the student {self.Name} regno number {self.regno} branch {self.branch} mentor name {self.mentorname} ")

# update=mentor("Yeshu",12312308,"CSE","Tharun")
# update.mentor_call()


