# 3. Find Sum of digits of a number using Recursion

# digit = int(input("Enter the digit to be evaluated:"))
def sum_of_digits(digit):
    if digit==0:
        return 0
    else:
        return digit%10+ sum_of_digits(digit//10)

# print(sum)
print(sum_of_digits(567))


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("Sum of digits:", result)
