#!/usr/bin/env python

def is_composite(n):
# Corner cases 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return False
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0): 
        return True
    i = 5
    while(i * i <= n): 
          
        if (n % i == 0 or n % (i + 2) == 0): 
            return True
        i = i + 6
    return False


def count_is_composite(numbers):
    composite_nums = 0
    for i in range (int(numbers)+1):
        if is_composite(i):
                composite_nums +=1
    return str(composite_nums)
   
def print_number():
    numbers = raw_input ("List of numbers you want to check: ")
    print "There are " + count_is_composite(numbers) + " composite numbers in the list"


#print_number()