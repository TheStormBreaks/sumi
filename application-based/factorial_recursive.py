# n! = n * (n-1)!
# 5! = 5 * 4!
# 4! = 4 * 3!
#......
# 0! = 1 

#define a function(factorial(number)) to compute the factorial of two numbers recursively

def factorial(number):
    # if the base case of the problem has reached then return the known result
    if number == 0:
        return 1 
    # else reduce the problem  further
    else:
        return number * factorial(number-1) # recursive function call (a function calling itself)
    
    
# invoking fuction factorial
print("Factorial :", factorial(2))