def hcf(a, b):
    #Iterative Approach
    smaller = a if a<b else b

    for i in range(1, smaller+1):
        if a%i == 0 and b%i==0:
            hcf = i

    return hcf

def hcf2(a, b):
#Euclidean Algorithm 
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b:
        return hcf2(a-b, b)
    return hcf2(a, b-a)

def hcf3(a, b):
#Euclidean Algorithm Efficient using Modulo Operator
    if b==0:
        return a
    else:
        return hcf3(b, a%b)

def lcm(a, b):
    #lcm using hcf
    lcm = (a*b)//hcf(a, b)
    return lcm

print(hcf(12,24))
print(hcf2(12,24))
print(hcf3(12,24))
print(lcm(12, 25))

