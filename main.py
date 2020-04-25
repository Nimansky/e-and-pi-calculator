import math
from decimal import *

#let user decide on how many decimal places of pi to display
digits = int(input("Number of decimal places of Pi to be calculated: "))  

#calculate pi to the n-th digit using the BBP-formula
def calc_pi(counter):
    return sum(1/Decimal(16)**k * (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)) for k in range(counter))
        
#set the precision of the decimals according to the desired number of decimal places;
#+3 because the formula seems to get every digit right except for the last 3
getcontext().prec = digits+3

#cut the last 3 extra digits
#also +2 so as not to include "3." in our x amount of digits
print(str(calc_pi(digits))[0:digits+2])