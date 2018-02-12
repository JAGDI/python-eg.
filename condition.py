from threading import Thread Condition
import time
import random

queue=[]
MAX_NUM=10
condition=condition()

class ProducerThread(Thread):
    def run(self):
        num=range(5)
        global queue
        while TRUE:
            condition.acquire()
            if len(Queue)==MAX_NUM:
                print("queuefull,producer is waiting")
                condition.wait()
                print("space in queue consumer notifiad the producer")
            num=random.choice(nums)
            queue("produced",num)
            condition.notify()
            condition.release()
            time.sleep(random.random())

class consumerThread(Thread):
     global queue
     while True:
         condition.acquire()
         if not queue:
                print("nothing is queue,consumer is waiting")
                condition.wait()
                print("producer added somthing to queue and notify the condumer")
         num=queue.pop(0)
         print("consumed",num)
         condition.notify()
         condition.release()
         time.sleep (random.random())
                            
producerThread().start()
consumerThread().start()
