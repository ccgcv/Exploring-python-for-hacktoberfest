arr = [1,9,8,7,0]
n = len(arr)

for i in range (0,n-1):

    min_index=i

    for j in range (i+1,n):

        if(arr[j]<arr[min_index]):
            min_index=j
    
    if(min_index != i):
        (arr[i],arr[min_index]) = (arr[min_index],arr[i])

print(arr)
