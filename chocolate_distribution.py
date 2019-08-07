#code
'''
ques
Given an array A of positive integers of size N, where each value represents number of chocolates in a packet. Each packet can have variable number of chocolates. There are M students, the task is to distribute chocolate packets such that :
1. Each student gets one packet.
2. The difference between the number of chocolates given to the students having packet with maximum chocolates and student having packet with minimum chocolates is minimum.
'''


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    a.sort()
    i = 0
    mindiff = float('inf')
    while i+m <= n:
        diff = a[i+m-1] - a[i]
        if diff < mindiff:
            mindiff = diff
        i += 1
    print(mindiff)
