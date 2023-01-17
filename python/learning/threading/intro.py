import threading
from queue import Queue
import time


def testThread(num):
    print(num)

def threadTest():
    # When this exits, the print_lock is released
    with print_lock:
        print(worker)

def threader():
    while True:
        # get the job from the front of the queue
        threadTest(q.get())
        q.task_done()

q = Queue()

if __name__ == '__main__':
    #for i in range(5):
            #t = threading.Thread(target=testThread, args=(i,))
            #t.start()
    for x in range(5):
        thread = threading.Thread(target = threader)
        thread.daemon = True
        thread.start()

    for job in range(10):
        q.put(job)