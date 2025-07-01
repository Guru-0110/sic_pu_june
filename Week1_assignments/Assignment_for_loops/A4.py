# # Right angled triangle 
# Num = int(input("Enter a number:"))
# for i in range(Num):
#     for j in range(i):
#         print("* ",end=" ")
#     print()

# # Equilateral Triangle
# Num = int(input("Enter a Number:"))
# for i in range(Num):
#         spaces=Num-i+1
#         stars=(2*i)+1
#         print(" "*spaces+"*"*stars)

# Hollow square



Num = int(input("Enter a number:"))
for i in range(Num):
         if i==0 or i == Num-1:
            stars = Num
            print("*"*stars)
         else:
            spaces =Num-2
            print("*"+" "*spaces+"*")


# Num=int(input())
# for i in range(Num):
#     stars = Num
#     print("* "*stars)


'''
    * * * *
   * * * *
  * * * * 
 * * * * 

'''

# Num = int(input("Enter the number:"))
# for i in range(Num):
#      spaces = Num-i+1
#      stars=Num
#      print(" "*spaces+"* "*stars)
     
'''
*   *
 * *
  *
 * *
*   * 

'''
# Num -i -3

# Num =int(input("Enter a Number:"))
# for i in range(Num):
#     spaces=i+1
#     between_spaces=(2*(Num-i-2)+1)
#     if between_spaces>0:
#         print(" "*spaces+"*"+" "*between_spaces+"*")
#     else:
#         print(" "*spaces+"*")

# for j in range(Num):
#     print(" "*(Num-j-1)+"*"+ " "*((2*j)+1)+"*")

