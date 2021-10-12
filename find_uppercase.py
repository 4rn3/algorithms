#given a string find the index of the first upper case letter in the string.

input_strng_1 = "pYthonAlgorithm"
input_strng_2 = "PythonAlgorithm"
input_strng_3 = "pythonalgorithm"

def find_uppercase_iterative(input_strng):
    for ch in input_strng:
        if ch.isupper():
            return ch
    return "no uppercase letters"

print(find_uppercase_iterative(input_strng_1))
print(find_uppercase_iterative(input_strng_2))
print(find_uppercase_iterative(input_strng_3))

def find_uppercase_recursive(input_strng, indx=0):
    if input_strng[indx].isupper():
        return input_strng[indx]
    if indx == len(input_strng)-1:
        return "no upper case letters"
    return find_uppercase_recursive(input_strng, indx+1) 

print(find_uppercase_recursive(input_strng_1))
print(find_uppercase_recursive(input_strng_2))
print(find_uppercase_recursive(input_strng_3))