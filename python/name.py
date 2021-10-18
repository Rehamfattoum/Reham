# name=input ("Enter your name")
# print("hello"+ name)
# num=int(input("enter number:")) 
# if num > 0:
#     print("The Number is positive")
# elif num < 0:
#     print("The Number is Negative")
# else:
#     print("Number is Zero")    

# name = input("Enter your name:")
# print(f"Hello {name} , How are you??")
# sister = ["reham","rita","yara","sara","rama"]
# print(sister)
# print(sister[2])
# sister.sort()
# sister.append("ali")
# sister.sort()
# print(sister)
# friends ={"key01":"Bilal","key02":"Nour"}
# sister = ["reham","rita","yara","sara","rama"]
# for i in range(4):
#     print(sister[i])
# def BMI ():
height=int(input("enter your height in cm please "))
weight=int(input("enter your weight in cm please "))
import datetime
age=datetime.datetime.now()
birth=int(input("please enter your birthday"))
print((f"your age is:{age.year-birth}") )
bmi=int()
bmi=weight/((height/100)*(height/100))
print(f"Your BMI is {round(bmi,2)}")
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<24.9:
    print("Normal weight")
elif bmi >=25 and bmi <29.9:
    print("Overweight")
else:
    print("Obesity")
