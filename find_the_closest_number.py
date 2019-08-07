#code
# ques is to find the closest number of k in array
# if 2 numbers give same difference then print the larger number

t = int(input())
for _ in range(t):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    mindiff = float('inf')
    i = 0
    while len(a)>2:
        n = len(a)
        if a[n//2]<k:
            diff = abs(k-a[(n//2)+1])
            if diff < mindiff:
                mindiff = diff
                i = a[(n//2)+1]
            elif diff == mindiff:
                if a[(n//2)+1]>i:
                    i = a[(n//2)+1]
                    
            diff = abs(k-a[n//2])
            if diff<mindiff:
                mindiff = diff
                i = a[n//2]
            elif diff == mindiff:
                if a[n//2] > i:
                    i = a[n//2]
            
            a = a[n//2:]
            
        elif a[n//2] == k:
            print(a[n//2])
            break
        
        else:
            diff = abs(k-a[n//2])
            if diff<mindiff:
                mindiff = diff
                i = a[n//2]
            elif diff == mindiff:
                if a[n//2]>i:
                    i = a[n//2]
                    
            a = a[:(n//2)+1]

    diff = abs(k-a[0])
    if diff< mindiff:
        mindiff = diff
        i = a[0]
    elif diff == mindiff:
        if a[0]>i:
            i = a[0]
            
    diff = abs(k-a[1])
    if diff < mindiff:
        i = a[1]
    elif diff == mindiff:
        if a[1]>i:
            i = a[1]
            
    print(i)
