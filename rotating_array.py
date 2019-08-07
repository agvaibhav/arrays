#code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = int(input())
    for i in range(d):
        res = a.pop(0)
        a.append(res)
    for j in a:
        print(j, end = ' ')
    print()
