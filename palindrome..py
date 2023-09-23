def main():
    pallindrome(313)


def pallindrome(n):
    sum=0
    a=n
    while n:
      
        rev=n%10
        sum=sum*10+rev
        n=n//10
    if sum==a:
        print("its pallidrome")
    else:
        print("its not pallindrome")    
        
        
main()            