#!/usr/bin/env python
#n = int(raw_input ("The number you want to check: "))
def is_prime(n):
    if n >= 2:
         for y in range (2,n):
                 if not (n % y):
                     return False
    else:
        return False
    return True

def print_number():
	n = int(raw_input ("The number you want to check: "))
	print(is_prime(n))

#print_number()


