from math import *
x=88
y='Mujahid'
z='Pock'
balance=0
def display():
    print(x,y,z)
    



def deposit():
    global balance
    depo=int(input('Enter amount to depoist'))  
    balance+=depo
    print('Current Balance is ',balance)

  
def fact():
    num=int(input('Enter number'))
    f=factorial(num)
    print('Factorial of ',num,' is ',f)  


def sq():
    num=int(input('Enter number to find its squre root'))
    f=sqrt(num)
    print('squre root of ',num,' is ',f)  


def pw():
    a=int(input('Enter number'))
    b=int(input('Enter number'))

    print(pow(a,b))

