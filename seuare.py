import multiprocessing
def cal_square(num,q):
     for n in num:
         q.put(n*n)

if __name__ == "__main__":
    num=[2,3,5]
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=cal_square,args=(num,q))
    p.start()
    p.join()
    while q.empty() is False:
        print(q.get())
