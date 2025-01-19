#Let us define a function by name gcd2
# The function gcd2 determines the greatest common divisior of two numbers

#Algorithm of gcd2(m,n)

#Step1:  Pass m, n as arguments to gcd1
def gcd2(m,n):

#Step3:  set the list of common factors of m and n factorsOf_mn to an empty list
    factorsOf_mn = []

#Step4: for i =1 to min(m,n)
#          if i is a factor of both m and append i to factorsOf_mn
    for i in range(1,min(m,n)+1):
        
        if ((m%i) == 0 and (n%i)== 0):
            factorsOf_mn.append(i)
         

#Step5:  determine the maximum factor in factorsOf_mn and return as the gcd
    return(factorsOf_mn[-1])