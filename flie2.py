def fac(f):
    fac=1
    for i in range(1,n):
        f=f*i
        i++
        print(f)
f1=open("dhi.txt","w")
n=int(input("enter no."))
w=fac(n)
f1.write(str(w))
f1.close()
