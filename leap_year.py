def is_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
 
years = [2000, 2004, 2009, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048] 
r = list(map(is_leap, years))
print(is_leap(2009))
print(r)