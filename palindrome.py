s = "Was it a cat I saw?"

def is_palindrome(s):
    i = 0 #start at the front
    j = len(s) - 1 #start at the back

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        
        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True

print(is_palindrome(s))