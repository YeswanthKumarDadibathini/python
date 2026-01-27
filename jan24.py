'''fruits={
    "orange":"orange",
    "mango":"yellow",
    "Apple":"Red",
    "Banana":"Yellow"
}
print(fruits)

d=dict(apple="red",mango="Yellow",orange="orange")
print(d)
print(type(d))

#To update and delet the keys or values
person={"names":"yeshu","age":20,"hobbie":"games"}
print(person)
person.pop("name")
print(person)'''

'''
data={
    'id':12312308,
    'info':{
        'name':'yeshu',
        'age':20,
        'course':'CSE'
    }
}
print(data)
print(data['info']['age'])
print(len('age'))'''

'''
student={'name':'yeshu','age':20,'grade':'A+'}
keys=student.keys()
values=student.values()
items=student.items()
print(keys)
print(values)
print(items)
'''
#To merge a two dict
'''
a={'a':1}
b={'b':2}
c=a|b
print(c)
'''
'''
student={
    'name':'yeshu',
    'age':20,
    'grade':'A+',
    'marks':[99,95,92]
}
another_student=student.copy()
student['marks'].append(98)
print(student)
print(another_student)'''

'''
import copy
student={
    'name':'yeshu',
    'age':20,
    'grade':'A+',
    'marks':[99,95,92]
}
another_student1=copy.deepcopy(student)
student['marks'].append(98)
print(student['marks'])
print(another_student1['marks'])


def fun(a,b):
    c=(a+b)
    print(a+b)
    print(a-b)
    print(a*b)
    print(c*c)
fun(1,2)

def build_profile(**things):
    print("Profiles")
    for i,j in things.items():
        print(i,j)
build_profile(name="yeshu",city="proddatur",country="india",)

import random

def game():
    number = random.randint(1, 20)
    while True:
        guess = int(input("Guess a number between 1 and 20: "))
        if guess == number:
            print("You guessed correct ")
            break
        else:
            print("Try again")

game()

'''
score=0
question1=["which one is the games launched mobile version"]
option=["A)free fire","B)COD","c)Pubg","D)Mortal combat"]
ans="A"
input1=input("enter your option:").upper()
if input1==ans:
    print("correct u got one point")
    score+=1
else:
    print("wrong")

ques2=["What is todays date"]
option2=["A)24","B)25","c)30","D)none"]
ans2='A'
input2=input("enter your option:").upper()
if input2==ans2:
    print("correct u got one point")
    score+=1
else:
    print("wrong")

ques3=["where state we are now"]
option3=["A)AP","B)TS","c)Punjab","D)none"]
ans3='C'
input3=input("enter your option:").upper()
if input3==ans3:
    print("correct u got one point")
    score+=1
else:
    print("wrong")

ques4=["where is LPU located"]
option4=["A)AP","B)TS","c)Punjab","D)none"]
ans4='C'
input4=input("enter your option:").upper()
if input4==ans4:
    print("correct u got one point")
    score+=1
else:
    print("wrong")

ques5=["in which state golden temple located"]
option5=["A)AP","B)TS","c)Punjab","D)none"]
ans5='C'
input5=input("enter your option:").upper()
if input5==ans5:
    print("correct u got one point")
    score+=1
else:
    print("wrong")

print("your total score",score)