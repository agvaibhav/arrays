'''
ques

Write a program to input a list of n integers in an array and arrange them
in a way similar to the to-and-fro movement of a Pendulum.

The minimum element out of the list of integers, must come
in center position of array. If there are even elements,
then minimum element should be moved to (n-1)/2 index (considering that indexes start from 0)
The next number (next to minimum) in the ascending order,
goes to the right, the next to next number goes to
the left of minimum number and it continues like a Pendulum.
'''



#code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    array = [None]*n
    a.sort()
    for i in range(0,n,2):
        array[(n-1-i)//2] = a[i]
        if n+1+i<2*n:
            array[(n+1+i)//2] = a[i+1]
    for j in array:
        print(j,end=' ')
    print()
