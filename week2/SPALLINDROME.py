n=input("string enter")
s=[]
for i in range(len(n)-1,-1,-1):
    s.append(n[i])# appending to array s
    r_str=''.join(s)#join back to string
if n==r_str:
    print("pallindrome")   
else:
    print("not pallindrome")     