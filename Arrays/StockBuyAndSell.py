def Sell(arr):
    
    n =len(arr)
    res = 0
    
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            res = max(res , arr[j]-arr[i])
    
    return res

if __name__ == "__main__":
    arr = [7, 10, 1, 3, 6, 9, 2]
    print(Sell(arr))