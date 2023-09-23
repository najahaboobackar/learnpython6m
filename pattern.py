for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print(" ")
    
for i in range(5):
    for j in range(i):
        print("#", end= " ")   
    print(" ")
    
print("     ")
for i in range(5,0,-1):
    for j in range(i):
        print("#", end= " ")   
    print(" ") 
    
print(" ")  
for i in range(5):
    print( " ")
    for j in range(i+1):
        print(" ",i, end= " ")   
    print(" ")             
    
    
for i in range(5):
    for j in range(i,5):
        print(" ", end="")
    for j in range(i+1):
        print("*",end=" ") 
    print()      
    
n=5
p=1
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
        p+=1 
    
    for j in range(i+1):
        print(p,end="")
        p-=1   
    print()          
        
        