#palindrome where the letters changed place

palin_perm1 = "tace cat"
palin_perm2 = "taco cat"

def is_pali_perm(s):
    s = s.replace(" ", "")
    s = s.lower() #normalize data

    d = dict()

    for i in s: #making dict of all lettes with frequency
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items(): #check if all values are even with max 1 char uneven
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

print(is_pali_perm(palin_perm1))