def maximumofthree(arr):
    
    max_product = -10**9;
    n = len(arr);
    
    for i in range(0,n-2,1):
        for j in range(i+1,n-1,1):
            for k in range(j+1,n,1):
                max_product = max(max_product,arr[i]*arr[j]*arr[k])
                
    print(max_product)
    
if __name__ == "__main__":
    
    arr = [1, -4, 3, -6, 7, 0]
    maximumofthree(arr)
                