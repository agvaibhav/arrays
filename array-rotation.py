import array
arr = array.array('i',[1,2, 3, 4, 5, 6])

# to print array
def print_array(arr):
    print("array is: ",end='')
    for i in range(len(arr)):
        print(arr[i],end=' ')
    print("")
                  
def array_rotation(arr,d):
    temp=[]
    for i in range(d):
        temp.append(arr[i])
    print(temp)
    n=d
    for i in range(len(arr)-d):
        arr[i]=arr[n]
        n+=1
    print_array(arr)
   
    for j in range(d):
        arr[-d]=temp[j]
        d-=1
    return(print_array(arr)) 


array_rotation(arr,2)
