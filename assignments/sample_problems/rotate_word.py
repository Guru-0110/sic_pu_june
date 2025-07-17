def isSameReflection(original_string, rotated_string):
    original_string= original_string+ original_string
    if rotated_string in original_string:
        return True
    else:        return False

print(isSameReflection("hello", "lohel"))  
print(isSameReflection("hello", "world"))  # False 