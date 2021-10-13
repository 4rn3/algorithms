def is_perm(s1,s2):
    s1 = s1.lower() #normalize data
    s2 = s2.lower() #normalize data

    if len(s1) != len(s2):
        return False

    d = dict()

    for i in s1:##making dict of all lettes with frequency
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
   
    for i in s2: #making dict of all lettes with frequency
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1        

    return all(value == 0 for value in d.values())# true if all letters have a value of 0

print(is_perm("tog", "god"))