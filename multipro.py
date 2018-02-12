import multiprocessing
def square(num,q):
    for n in num:
        q.put(n*n)

if __name__ == "__main__":
    num=[2,3,5]
    q=multiprocessing.Queue()
    m=multiprocessing.Process(target=square.args=(num,q))
    m.start()
    m.join()
    while q.empty() is False:
                  print(q.get())
