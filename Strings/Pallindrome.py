def palindrome(str):
    
    n =len(str)

    str1 = ""
    for i in range(n-1,-1,-1):
        str1 += str[i]
       
        
    if(str==str1):
        return True
    
    return False

if __name__ == "__main__":
    str = "abba"
    print(palindrome(str))
        
        