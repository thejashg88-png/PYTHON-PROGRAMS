def Maximun(arr):
    
    count = 1;
    max_count = 0;
    
    for i in range(1,len(arr),1):
        
        if(arr[i]==arr[i-1]):
            count += 1
        else:
            max_count =max(max_count,count)
            count = 1
    
    max_count = max(max_count,count)
    print(max_count)

if __name__ =="__main__":
    arr = [1,0,0,1,1,1,0,0]
    Maximun(arr)
    
    