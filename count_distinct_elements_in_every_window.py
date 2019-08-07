'''
ques
Given an array A[] of size N and an integer K. Your task is to
complete the function countDistinct() which prints the
count of distinct numbers in all windows of size k in the array A[].

'''


def countDistinct(arr, n, k):
    # Code here
    i = 0
    while i+k<=n:
        count = {}
        for j in range(i,i+k):
            if not arr[j] in count:
                count[arr[j]] = 1
        print(len(count), end = ' ')
        i += 1
        
    print()

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        n,k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        countDistinct(arr, n, k)
