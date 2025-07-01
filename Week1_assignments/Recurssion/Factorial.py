# Number=5
def fact(Number):
    if Number==1 or Number==0:
        return 1
    else:
        return Number*fact(Number-1)

print(fact(5))