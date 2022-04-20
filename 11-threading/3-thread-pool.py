import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import random

def test(item):
    s=random.randrange(1,10)
    logging.info(f"Thread {item} : id ={threading.get_ident()}")
    logging.info(f"Thread {item} : name ={threading.current_thread().name}")
    logging.info(f"Thread {item} : Sleepin for {s} second(s)")
    time.sleep(s)
    logging.info(f"Thread {item} : Finished")

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S',level=logging.DEBUG );
    logging.info("App Start")

    workers=5
    items=15

    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(test,range(items))

    logging.info("App Finished")


main()