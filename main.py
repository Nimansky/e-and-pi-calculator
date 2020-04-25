digits = input("Number of decimal places of Pi to be calculated: ")

def calc_pi(counter):
    if counter > 0:
        newnum = ((-1)**counter)/((2*counter)+1)
        total = newnum + calc_pi(counter-1)
        
#def display_pi(places):
 #   print
while true:
    calc_pi(digits)
    