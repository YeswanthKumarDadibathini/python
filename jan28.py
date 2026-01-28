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

class bank:
    def __init__(self,bankACC,branch,withdraw,balance):
        self.bankACC=bankACC
        self.branch=branch
        self.withdraw=withdraw
        self.__balance=balance
    def bankdet(self):
        print(f"The bank account number {self.bankACC} and branch name {self.branch} amount to withdraw {self.withdraw} the remainind balance {self.__balance} ")

    def get_balance(self):
        return self.__balance 

details=bank(123456789,"Kadapa",10000,90000)
details.bankdet()

class cars:
    def __init__(self,car_model,owner_name,branch,carplate):
        self.car_model=car_model
        self.owner_name=owner_name
        self.branch=branch
        self.__carplate=carplate
    def car_del(self):
        print(f"model of the car {self.car_model} owners name {self.owner_name} location of the branch {self.branch} and car plate {self.__carplate} ")
    
    def get_plate(self):
        return self.__carplate

detailss=cars('BMW','yeshu','kadapa',1)
detailss.car_del()