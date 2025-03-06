# Joseph Jose A. Deysolong
# CS3A

import threading
import concurrent.futures
import time
import random
import math

def do_task(thread_id):
    print(f"Thread {thread_id} stared")
    time.sleep(random.randint(1,3))
    print(f"Thread {thread_id} finished")

def main():
    threads = []
    num_threads = 5
    
    for i in range(num_threads):
        t = threading.Thread(target=do_task, args=(i,))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
    
    print("All threads have completed")
    

if __name__ == '__main__':
    main()


