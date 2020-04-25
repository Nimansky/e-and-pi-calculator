import math
from decimal import *
import sys

#make it so the user can calculate e up to x digits, although python seems to cap this method at 1904 digits
sys.setrecursionlimit(20000)

#let user decide on how many decimal places of pi to display
mode = int(input("e or pi (1 or 2)? "))
digits = int(input("Number of decimal places to be calculated: "))  

#Calculate pi to the n-th digit using the BBP-formula
def calc_pi(counter):
    return sum(1/Decimal(16)**k * (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)) for k in range(counter))

def factorial(number):
    if number > 1:
        return number*factorial(number-1)
    else:
        return 1

#Calculate e to the n-th digit using the Brothers' formula
def calc_e(counter):
    e = Decimal(2)
    for i in range(1,counter+1):
        num = Decimal(2*i+2)
        denom = Decimal(factorial(2*i+1))
        e += Decimal(num/denom)
    return e
    
#set the precision of the decimals according to the desired number of decimal places;
#+3 because the formula seems to get every digit right except for the last 3
getcontext().prec = digits+3

#cut the last 3 extra digits
#also +2 so as not to include "3." / "2." in our x amount of digits
if mode == 1:
    print(str(calc_e(digits))[:digits+2])
if mode == 2:
    print(str(calc_pi(digits))[:digits+2])