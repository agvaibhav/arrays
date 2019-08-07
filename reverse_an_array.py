#code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        print(a[n-1-i], end=' ')
    print()
