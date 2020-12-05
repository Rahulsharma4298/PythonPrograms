def adams_charity(N):
    sum = 0
    for i in range(1, N+1):
        sum += i**2
    return sum

print(adams_charity(5))
print(adams_charity(2))
print(adams_charity(51))
print(adams_charity(501))
