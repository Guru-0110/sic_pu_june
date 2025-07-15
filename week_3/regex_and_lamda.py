# import re

# data = ["abc123", "hello2024", "no digits", "zip007"]

# # Extract digits using regex and lambda
# digits = list(map(lambda s: re.findall(r'\d+', s), data))
# print(digits)  # [['123'], ['2024'], [], ['007']]


# d = digits = + = for any number of occurenecces from the data s 

import re

# data = ["Hello123", "A@B#C", "Clean_text", "X Y Z"]

# # Remove all non-alphabetic characters
# cleaned = list(map(lambda s: re.sub(r'[^a-zA-Z]', '', s), data))
# print(cleaned)  # ['Hello', 'ABC', 'Cleantext', 'XYZ']


# emails = ["alice@gmail.com", "bob@yahoo.com", "user@outlook.com"]

# # Extract domain using regex
# domains = list(map(lambda s: re.search(r'@(\w+)\.', s).group(1), emails))
# print(domains)  # ['gmail', 'yahoo', 'outlook']


words = ["apple", "banana", "orange", "grape", "umbrella"]

# Capitalize if starts with a vowel
vowel_caps = list(map(lambda w: re.sub(r'^[aeiou](\w+)',upper(), w), words))
print(vowel_caps)  # ['Apple', 'banana', 'Orange', 'grape', 'Umbrella']