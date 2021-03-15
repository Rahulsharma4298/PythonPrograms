# Method 1 (Using Slicing/substr() function)
def substring(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)+1): # len(string)+1 because at last i+1 & len(string) will be same, so it will not be included
            print(string[i:j])

substring("abcd")

# Method 2 (Generate a substring using previous substring):-
def substring(s, n):
    for i in range(n):
        temp = ""
        for j in range(i, n):
            temp += s[j]
            print(temp)
s = "abcd"        
substring(s, len(s))

# Method 3 (using three nested loops):-
def substring(s, n):
    # this is for the selection
    # of starting point
    for i in range(n):
        # 2nd for loop is for selection
        # of ending point
        for j in range(i, n):
             # 3rd loop is for printing from
            # starting point to ending point
            for k in range(i, (j+1)):
                print(s[k], end="")
            # changing the line after printing
            # from starting point to ending point
            print()

substring(s, len(s))

    
            
                    
