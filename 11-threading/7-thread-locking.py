import logging
import threading
from concurrent.futures import  ThreadPoolExecutor
import  time
import random


counter=0

def test(count):
    global counter
    thread_name=threading.current_thread().name
    logging.info(f"Starting : {thread_name}")

    for x in range(count):
        logging.info(f"Count: {thread_name} += {count}")
        # # The Global Interpreter Lock (GIL) in action
        # counter+=1

    #     Locking
    #     lock=threading.Lock()
    #     lock.acquire()
    #     lock.acquire() # deadlock -- waiting on the resources
    #     try:
    #         counter+=1
    #     finally:
    #         lock.release()
    # Locking Simplified
        lock=threading.Lock()

        with lock:
            logging.info(f"Locked : {thread_name}")
            counter+=1
            time.sleep(2)



    logging.info(f"Completed: {thread_name}")

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S',level=logging.DEBUG );
    logging.info("App Start")
    workers=2
    with ThreadPoolExecutor(max_workers=2) as executor:
        for x in range(workers):
            v=random.randrange(1,5)
            executor.submit(test,v)
    print(f"Counter: {counter}")
    logging.info("App Finished")

main()


# https://hackernoon.com/has-the-python-gil-been-slain-9440d28fa93d?gi=f4ce28a38d5