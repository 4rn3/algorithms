#given a string calculate the length of the string.

input_str = "python"

def iterative_str_length(input_str):
    count = 0
    for ch in input_str:
        count += 1
    return count

def recursive_str_length(input_str):
    if input_str == '':
        return 0
    return 1+recursive_str_length(input_str[1:])

print(iterative_str_length(input_str))
print(recursive_str_length(input_str))