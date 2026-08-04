def majority(arr):
    
    n = len(arr)
    
    for i in range(n):
        count = 0;
        for j in range (n):
            if arr[i]==arr[j]:
                count += 1
            
        if count > n/2:
            return arr[i]
        
    return -1

if __name__ =="__main__":
    arr = [1, 2, 2, 1, 3, 2, 2]
    print(majority(arr))