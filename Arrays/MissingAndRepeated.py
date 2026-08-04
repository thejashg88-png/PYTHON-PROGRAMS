def missrepea(arr):
    
    n = len(arr)
    
    freq = [0]*(n+1)
    missing = -1
    repeating = -1
    
    for i in arr:
        freq[i] += 1
        
    for i in range(1,n+1):
        if(freq[i]==0):
            missing = i
        elif(freq[i]==2):
            repeating = i
    
    print(missing,repeating)
    
if __name__ == "__main__":
    arr = [4, 3, 6, 2, 1, 1]
    missrepea(arr)            
        
    
    