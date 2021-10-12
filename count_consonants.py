input_str_1 = "abc de"
input_str_2 = "Python"

def iterative_consonant_count(input_str):
    ctr = 0
    for ch in input_str:
        if ch not in ['a','e','i','o','u'] and ch.isalpha():
            ctr +=1
    return ctr

print(iterative_consonant_count(input_str_1))
print(iterative_consonant_count(input_str_2))

def recursive_consonant_count(input_str):
    if input_str == '': 
        return 0
    if input_str[0].lower() not in ['a','e','i','o','u'] and input_str[0].isalpha():
        return 1 + recursive_consonant_count(input_str[1:])
    else:
        return recursive_consonant_count(input_str[1:])

print(recursive_consonant_count(input_str_1))
print(recursive_consonant_count(input_str_2))