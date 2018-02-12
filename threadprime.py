import threading
def prime():
    f=0
    i=1
    if(n%2==0):
        f=1
    else:
        f=0
    if(f==1):
        print("this in not prime no.")
    else:
        print("prime no")

if __name__ == "__main__" :
    n=int(input("enter no."))
    t=threading.Thread(target=prime)
    t.start()
    t.join()
    print("done")
