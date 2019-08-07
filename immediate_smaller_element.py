#code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.append(-1)
    for i in range(n):
        if a[i+1]<a[i]:
            print(a[i+1],end=' ')
        else:
            print(-1,end=' ')
    print()
