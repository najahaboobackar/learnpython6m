def main():
     for _ in primegen(10):
        pass
    
def prime(n):
    for i in range(2,n+1):
        if n%i==0:
            return False
        else:
            return True  
 
def primegen(a):
   for i in range(2,a+1) :
    if prime(i):
        yield i
        print(i)   
        
main()            