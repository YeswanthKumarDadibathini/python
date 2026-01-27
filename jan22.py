'''passw=int(input("enter the password: "))
while True:
    password=123456
    if passw==password:
        print(passw,"You Enter the correct pass")
        break
    else:
        print("System was locked")
        break


cash=int(input("Enter the cash: "))
if (cash >= 200 and cash %100==0 and cash!=300):
    print("Discharge cash")
else:
    print("not available cash")'''


time=int(input("Enter the time: "))
if 1<=time<=5:
    print("sleep")
elif 6<=time<=11:
    print("Good morning")
elif 12<=time<=17:
    print("good afternoon")
elif 18<=time<=20:
    print("good evening")
elif 21<=time<=23:
    print("good night")
else:
    print("invalid time")