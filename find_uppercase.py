#given a string find the index of the first upper case letter in the string.

input_strn_1 = "pYthonAlgorithm"
input_strn_2 = "PythonAlgorithm"
input_strn_3 = "pythonalgorithm"

def find_uppercase_iterative(input_strn):
    for ch in input_strn:
        if ch.isupper():
            return ch
    return "no uppercase letters"

print(find_uppercase_iterative(input_strn_1))
print(find_uppercase_iterative(input_strn_2))
print(find_uppercase_iterative(input_strn_3))

def find_uppercase_recursive(input_strn, indx=0):
    if input_strn[indx].isupper():
        return input_strn[indx]
    if indx == len(input_strn)-1:
        return "no upper case letters"
    return find_uppercase_recursive(input_strn, indx+1) 

print(find_uppercase_recursive(input_strn_1))
print(find_uppercase_recursive(input_strn_2))
print(find_uppercase_recursive(input_strn_3))