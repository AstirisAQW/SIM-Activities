# Joseph Jose A. Deysolong
# CS3A

#Part 1
import sys
print(sys.version)
# Check if the following basic Python Libraries are installed.
import os
import sys
import math
import random
import datetime
import re
import json
import collections

import itertools

# Verify if the following advanced libraries are installed
import numpy
import pandas
import scipy
import sklearn
import tensorflow as tf
import torch
import keras
import matplotlib
import seaborn
from bs4 import BeautifulSoup
import scrapy
import nltk
import cv2

#Verify for the PARALLEL and DISTRIBUTED Computing Libraries
import multiprocessing
import concurrent.futures
import threading
import asyncio

# Third-Party Libraries
import mpi4py
import dask
import ray
import joblib
import celery



#Part 2
import random
import string

def generate_password():
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password_length = random.randint(8, 16)

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password with random characters from the full pool
    password += random.choices(all_characters, k=password_length - 4)

    # Shuffle the password to ensure it's random
    random.shuffle(password)

    # Join the list into a string
    return ''.join(password)

# Generate and display the password
password = generate_password()
print(f"Your new password is: {password}")
