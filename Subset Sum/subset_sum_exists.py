def subSum(arr,target):
    n = len(arr)
    dp = [[None]*(target+1) for _ in range(n+1)]
        
    for i in range(target+1):
        dp[0][i] = False
    for j in range(n+1):
        dp[j][0] = True

    # An element can be chosen only if sum is less han arr[i] else it cannot be included
    for i in range(1,n+1):
        for j in range(target+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target]

if __name__ == '__main__':
    arr = []  
    
    n = int(input("Enter number of elements : "))
    
    for i in range(0, n):
        ele = int(input())  
        arr.append(ele) 
    target = int(input("Enter target sum : "))
    exists =  subSum(arr,target)
    print('Subset with Target sum exists : ', str(exists))