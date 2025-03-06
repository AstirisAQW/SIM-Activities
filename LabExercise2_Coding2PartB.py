# Joseph Jose A. Deysolong
# CS3A

import threading
import concurrent.futures
import time
import random
import math

def compute_square(n):
    return n * n

def data_parallel():
        numbers = list(range(1,11))
        with concurrent.futures.ProcessPoolExecutor() as executor:
                results = list(executor.map(compute_square, numbers))
                
        for num, square in zip(numbers, results):
            print(f"{num} squared is {square}")

if __name__ == '__main__':
    print("Running data-parallel example:")
    data_parallel()