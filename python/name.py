from datetime import date
from tkinter import *
# import sys
# from function import sum
# from function import min
# from function import multi
# from function import div
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
# height=int(input("enter your height in cm please "))
# weight=int(input("enter your weight in cm please "))
# import datetime
# age=datetime.datetime.now()
# birth=int(input("please enter your birthday"))
# print((f"your age is:{age.year-birth}") )
# bmi=int()
# bmi=weight/((height/100)*(height/100))
# print(f"Your BMI is {round(bmi,2)}")
# if bmi<18.5:
#     print("Underweight")
# elif bmi>=18.5 and bmi<24.9:
#     print("Normal weight")
# elif bmi >=25 and bmi <29.9:
#     print("Overweight")
# else:
#     print("Obesity")
# number1= int(input("please enter the number1 : "))
# number2= int(input("please enter the number2 : "))
# operation=input("please enter the operation : ")

# try:
#    number1= int(input("please enter the number1 : "))
#    number2= int(input("please enter the number2 : "))
#    operation=input("please enter the operation : ")
# except ValueError:
#     print ("please don't enter Syntax ")
#     sys.exit (0)
# if operation=="+":
#     sum (number1,number2)
#     print(sum(number1,number2))
# elif operation=="-":
#     min (number1,number2)
#     print(min(number1,number2))
# elif operation=="*":
#     multi (number1,number2)
#     print(multi(number1,number2))
# elif operation=="/" and number2!=0:
#     div (number1,number2)
#     print(div(number1,number2))
# else:
#     print("please enter the operation")
# class Point () :
#     def __init__ (self,input1,input2):
#         self.x = input1
#         self.y = input2
# p = Point(8,2)
# print(p.x)
# print(p.y)
# class Flight ():
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.passengers=[]

#     def add_passengers (self,name)
#     if not open_seat ()
#         self.passengers.append(name)
#         return true
    
#     def open_seat (self)
#     self.capacity - Len(self.passengers)
#     return

# Flight = Flight(4):
# ("reham","rita","ali","yara","sara")

main_window = Tk()
Label(main_window,Text="year of birthday").pack().grid(row=0,column=0)
year=Entry(main_window,width= 50 ,borderwidth=5).grid(row=0,column=1)
Label(main_window,Text=" month of birthday").pack().grid(row=1,column=0)
month=Entry(main_window,width= 50 ,borderwidth=5).grid(row=1,column=1)
Label(main_window,Text="day of birthday").pack().grid(row=2,column=0)
day=Entry(main_window,width= 50 ,borderwidth=5).grid(row=2,column=1)
Button(main_window,text="My age" ,command=onclick).grid(row=3,column=0)
def onclick ():
    if age.month==month and age.day==day:
        print(("Happy Birthday") )
    else:
        print((f"your age is:{age.year-year}") )

main_window.mainloop() 


# age=date.today()
# year=int(input("enter your year of birthday"))
# month=int(input("enter your month of birthday"))
# day=int(input("enter your day of birthday"))
# if age.month==month and age.day==day:
#     print(("Happy Birthday") )
# else:
#     print((f"your age is:{age.year-year}") )