# Using Iteration

def rev1(s):
	j = len(s)-1
	rev = ""
	while j >= 0:
		rev = rev + s[j]
		j -= 1
	return rev

def rev2(s):
	rev = ""
	for i in s:
		rev = i + rev
	return rev

# Using Recursion

def rev_rec(s):
	if len(s) == 0:
		return s
	else:
		return rev_rec(s[1:]) + s[0]

# Using builtin function

s = "hello"
print("".join(reversed(s)))
print(rev1(s))
print(rev2(s))
print(rev_rec(s))