L = [2,3,4,5]
R = [1,6,7]
arr = [None]*len(L+R)

i = j = k = 0
while i<len(L) and j<len(R):
    if L[i] < R[j]:
        arr[k] = L[i]
        i+=1
        k+=1
    else:
        arr[k] = R[j]
        j+=1
        k+=1

while i<len(L):
    arr[k] = L[i]
    i+=1
    k+=1
            
while j<len(R):
    arr[k] = R[j]
    j+=1
    k+=1
    
print(arr)