def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    d = dict()
    
    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for j in s2:
        if j in d:
            d[j] -= 1
        else:
            d[j] = 1

    for i in d:
        if d[i] != 0:
            return False
    return True

s1 = "listen"
s2 = "silent"

print(is_anagram(s1, s2))

s1 = "fairy tales"
s2 = "rail safety"

print(is_anagram(s1, s2))

    
    
    
