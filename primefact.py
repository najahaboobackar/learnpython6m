def main():
    n=int(input("enter the number"))
    factor(n)


def factor(a):
    for i in range(2,a+1):
        if a%i==0:
            print(i) 
            

main()              