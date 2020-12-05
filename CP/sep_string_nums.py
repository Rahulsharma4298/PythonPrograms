nums = "0123456789"
spl_chars = "!@#$%^&*()-_=+[]{}';\|,.?/"
string = "a2b5bc789@z#*"
nums_list = []
alpha = []
spl_chars_list = []


for i in string:
    if i in nums:
        nums_list.append(i)
    elif i in spl_chars:
        spl_chars_list.append(i)
    else:
        alpha.append(i)

print(*alpha, sep="")
print(*nums_list, sep="")
print(*spl_chars_list, sep="")
