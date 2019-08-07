#code
t = int(input())
for _ in range(t):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    i=0
    while i<n:
        last_index = i+k-1
        if last_index>=n:
            last_index = n-1
        for j in range(last_index,i-1,-1):
            print(a[j],end=' ')
        i = i+k
    print()
