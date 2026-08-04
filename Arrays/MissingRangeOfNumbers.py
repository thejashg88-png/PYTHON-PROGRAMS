def missing(arr,lower,upper):
    
    n = len(arr)
    new_arr = []
    
    if lower<arr[0]:
        new_arr.append([lower,arr[0]-1])
        
    for i in range(n-1):
        if arr[i+1]-arr[i]>1:
            new_arr.append([arr[i]+1,arr[i+1]-1])
            
    if upper > arr[-1]:                                 #Here arr[-1] gives last element i.e in this case 45
        new_arr.append([arr[-1] + 1, upper])
        
    for i in new_arr:
        print(i[0],i[1])
        
if __name__ == "__main__":
    arr = [14, 15, 20, 30, 31, 45]
    lower = 10
    upper = 50
    missing(arr,lower,upper)
            
    
            
    
        