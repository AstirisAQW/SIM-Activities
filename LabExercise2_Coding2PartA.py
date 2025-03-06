# Joseph Jose A. Deysolong
# CS3A

import threading
import concurrent.futures
import time
import random
import math

def simulate_io_task(task_id):
    print(f"Task {task_id} started")
    time.sleep(2)
    return f"Task {task_id} completed"

def task_parallel():
    with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as executor:
        futures = [executor.submit(simulate_io_task, i) for i in range(5)]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == '__main__':
    print("Runnign task-parallel example:")
    task_parallel()