# Series 
N = int(input("enter the numbers between 1 and 4:"))
M = int(input("enter the numbers between 1 and 10:"))
sum_term=0
sign = -1
for i in range(M):
    Numerator = N**2**i
    sign = -1 * sign
    Denominator = 2*i+1
    terms =((Numerator)/(Denominator))*sign
    sum_term += terms

print(sum_term)