#code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    odd = []    
    even = []
    for i in a:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    odd.sort(reverse = True)
    even.sort()
    final = odd + even
    for i in final:
        print(i,end=' ')
    print()
