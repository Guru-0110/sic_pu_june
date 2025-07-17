Number=int(input("Enter the Number :"))
a=1
b=2
def A():
    print(a)
def B():
    print(b)
for i in range(Number):
    if i==0:
        A()
    elif i==1:
        B()
    else:
        C=a+b
        print(C)
        a=b
        b=C

