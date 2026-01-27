'''a=1
b=3
c=a+b
b=a-b
print(c)
age=25
Age=30
print(age,Age)



a=25
b="hello"
c=25.0
d=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))



number=int(input("Enter the number: "))
if number % 2 ==0:
    print("It is a even")
else:
    print("it is a odd")
num=55
print(num*num)



name=str(input("Enter the name of the student: "))
eng=int(input("marks in eng: "))
maths=int(input("marks in maths:"))
science=int(input("marks in science:"))
total=(eng+maths+science)
print(total)
avg=total/3
print(avg)
print("result of the exam")



person=str(input("enter the name of the person: "))
item=str(input("name of the item: "))
price=int(input("price of the item: "))
quantity=int(input("how much quantity: "))
cost=price*quantity
print(price)
gst=price*quantity*0.18
print(gst)
total=price+gst
print(total)'''



a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
if a>b and a>c:
    print("A is the biggest")
elif b>a and b>c:
    print("B is the biggest")
else:
    print("C is the biggest")