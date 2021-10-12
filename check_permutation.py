def is_perm(s1,s2):
    s1 = s1.lower() #data normaliseren
    s2 = s2.lower() #data normaliseren

    if len(s1) != len(s2):
        return False

    d = dict()

    for i in s1: #dictionary maken van alle letters & kijken hvl keer ze voorkomen -> char in alle 2 de woorden = 0 anders 1
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
   
    for i in s2: #dictionary maken van alle letters & kijken hvl keer ze voorkomen -> char in alle 2 de woorden = 0 anders 1
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1        

    return all(value == 0 for value in d.values())# true als alle letters waarde v 0 hebben

print(is_perm("tog", "god"))