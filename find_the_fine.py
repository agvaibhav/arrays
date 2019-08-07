#code
'''
ques
Given an array of penalties P, an array of car numbers C,
and also the date D. The task is to find the total fine
which will be collected on the given date.
Fine is collected from odd-numbered cars on even dates and vice versa.

'''

t = int(input())
for _ in range(t):
    n,d = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = list(map(int, input().split()))
    stack = []
    if d%2 == 0:
        for i in range(n):
            if c[i]%2!=0:
                stack.append(i)
    else:
        for i in range(n):
            if c[i]%2==0:
                stack.append(i)
    sum = 0
    for index in stack:
        sum += p[index]
    print(sum)
