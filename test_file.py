# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:10:42 2020

@author: NG18
"""

import pandas as pd
import numpy as np
import datetime, time

print("today's date:", datetime.date.today())

print("today's date:", datetime.datetime.now())

for i in range(10):
    print("today's date:", datetime.datetime.now())
    time.sleep(0.5)