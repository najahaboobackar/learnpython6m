def main():
   
    atm()



def atm():
    a=int(input("enter the number 1 to deposit 2 to withdraw"))
    bal=500
    if a==1:
        b= int(input("enter the amount to be deposited"))
        bal=bal+b
        print(bal,":balance")
    elif a==2:
        c=int(input("enter the maount to be withdraw")) 
        if(c>bal):
            print("sorry not enough balance") 
        else:
            bal=bal-c
            print(bal,"balance")
     
        
        
main()                  