def main():
    amstrong(13)
    
def amstrong(n):
    
  
    s=n%10
   
    b=int(n/10)
  
    y=b%10
   
    c=int(b/10)
   
    z=c%10
    
    a=s**3 + y**3 +z**3
    print(a)
    if a==n:
        print("amstrong")
    else:
        print("not")    
        
             
 
 
        
main()       