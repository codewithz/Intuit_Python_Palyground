import concurrent.futures
import time
import threading
from concurrent.futures import ThreadPoolExecutor

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds}  second(s)....')
    time.sleep(seconds)
    return "Done Sleeping"

with ThreadPoolExecutor() as executor:
    results=[executor.submit(do_something,1) for _ in range(10)]

    for future in concurrent.futures.as_completed(results):
        print(future.result())


# threads=[]
#
# for _ in range(10):
#     t=threading.Thread(target=do_something,args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

finish=time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")