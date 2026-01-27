#name=input("Enter your name: ")
#age=input("Enter your age: ")
#message=input("write message ")
#print(name,age,message)
#import math as m
#print(m.pi)
"""
a =4
b =5
a=a+b
b=a-b
a=a-b
print(a,b)

number=int(input("Enter the number: "))
if number % 2 ==0:
    print("it is even ")
else:
    print("it is odd ")

num=int(input("Enter the number: "))
for i in num:
    if i==1 and i%num==0:
        print("it is prime number")
    else:
        print("it is not a prime number")
        
num = int(input("Enter the number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

num=int(input("table no: "))
for i in range(0,11):
    print(num,"X",i+1,"=",num*(i+1))
    
a, b = 0, 1
print(a, b, end=" ")

for _ in range(8):
    c = a + b
    print(c, end=" ")
    a, b = b, c

num=int(input("Enter the number: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime no")
            break
    else:
            print(num,"is a prime no")
else:
        print(num,"is not a prime no")
        
a,b=0,1
print(a,b,end=" ")
for _ in range(8):
    c=a+b
    print(c,end=" ")
    a,b=b,c
    """
"""
a, b = 0, 1
print(a, b, end=" ")

for _ in range(8):
    c = a + b
    print(c, end=" ")
    a, b = b, c

a,b=0,1
print(a,b,end=" ")

for _ in range(8):
    c=a+b
    print(c,end=" ")
    a,b=b,c

num=int(input("Enter the number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    """
#double=lambda x:x * 2
#print(double(6))
'''
def appl(fx,value):
    return 6+fx(value)

cube=lambda x:x*x*x
print(appl(cube,2))

def factoral(n):
    if n==0:
        return 1
    else:
        return n*factoral(n-1)
print(factoral(4))


def sqrt_num(fun,x):
    return fun(x)
sque=lambda n:n*n
print(sqrt_num(sque,2)) 
t = ("disco", 12, 4.5)
print(t[0][2])
word = ['1','2','3','4']
word[ : ] = [ ] 
print(word)
L = ['one','two','three', 'four', 'five', 'six']
print(sorted(L))
print (L)
d = {0: 'Fish', 1: 'Bird', 2: 'Mammal'}
for i in d:
    print(i, end = " ")'''
ordinary_dict ={}

for i in range(2,21):
    if i % 2 == 0:
        ordinary_dict[i] = i**2

print(ordinary_dict)

updated_dict = {i : i**2 for i in range(2,21) if i % 2 ==0}
print(updated_dict)