#palindrome waar de letters van plaats veranderd zijn

palin_perm1 = "tace cat"
palin_perm2 = "taco cat"

def is_pali_perm(s):
    s = s.replace(" ", "")
    s = s.lower() #data normaliseren

    d = dict()

    for i in s: #dictionary maken van alle letters & kijken hvl keer ze voorkomen
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items(): #controleert als iedere value een even aantal keer voorkomt met max 1 on even char= taco cat -> 2x c , a, t en 1x o anders False
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

print(is_pali_perm(palin_perm1))