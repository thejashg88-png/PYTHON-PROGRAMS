def Add(arr):
    
    n = len(arr)
    num = 0
    for i in range(n):
        num = num*10+arr[i]
        
    print(num+1)

if __name__ == "__main__":
    arr = [1,2,4]
    Add(arr) 