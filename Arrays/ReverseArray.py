def reverse_array(arr):
    n = len(arr)
    reverse_array = []
    
    for i in range(n-1,-1,-1):
        reverse_array.append(arr[i])
        
    for i in range(n):
        print(reverse_array[i])
        
if __name__ == "__main__":
    arr = [10,20,30,40,50]
    reverse_array(arr)
    