'''
Equilibrium position in an array is a position such that
the sum of elements before it is equal to the sum of elements after it.
'''

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sum_front = a[0]
    sum_back = a[-1]
    i = 0
    j = 0
    if n==1:
        print(1)
    elif n==2:
        print(-1)
    elif n==3:
        if a[0]==a[-1]:
            print(2)
    else:
        while i+j<(n-3):
            if sum_front > sum_back:
                j += 1
                sum_back += a[n-1-j]
            elif sum_front < sum_back:
                i += 1
                sum_front += a[i]
            elif sum_front == sum_back:
                i += 1
                j += 1
                sum_front += a[i]
                sum_back += a[n-1-j]
        if sum_front == sum_back:
            print(i+2)
        else:
            print(-1)
