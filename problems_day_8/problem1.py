char1=input("Enter the String to be rotated:")
char2= input("Enter the rotated String:")

temp_string=char2*2
print(temp_string)

if temp_string.__contains__(char1):
    print(1)
else:
    print(-1)

if temp_string.find(char1):
    print(1)
else:
    print(-1)
