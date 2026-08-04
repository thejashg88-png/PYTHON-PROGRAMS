def sort(arr):
    
    n = len(arr)
    
    for i in range(0,n-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    
    for i in range(n):
        print(arr[i])
        
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]  
    sort(arr)
        
        