v=("a","e","i","o","u")
f1=input("enter file name:")
f0=open(f1,"r")
re=f0.readlines()
i=1
numv=0
for l in re:
    print("line:",i)
    for c in l:
        if c in v:
            numv+=1
    print("vowels in line:",numv)
    i+=1
f0.close()
