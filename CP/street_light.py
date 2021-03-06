"""
One of the streets in your city has a total of L street lights.
Each light i covers the street from Xi to Yi distance.
Find the length of street covered with light.

input1: 2,
input2: {{5,10}, {8, 12}}

streetlight1: 10 - 5 = 5
streetlight2: 12 - 8 = 4
common region: 10 - 8 = 2
Total = 5 + 4 - 2 = 7

output: 7

"""


def street_light(input1, input2):
    out = []
    for i in input2:
        for j in range(i[0], i[1]):
            out.append(j)

    a = set(out)
    print(len(a))

def street_light2(input1, input2):
    result = 0
    for i in range(input1):
        a = (input2[i][1] - input2[i][0])
        result += a
        try:
            if input2[i+1][0] < input2[i][1]:
                s = input2[i][1] - input2[i+1][0]
                result -= s
        except IndexError:
            break
    print(result)
        

ip1 = 2
ip2 = [[5,10], [8,12]]
street_light2(ip1, ip2)

ip1 = 1
ip2 = [[5,10]]
street_light2(ip1, ip2)


