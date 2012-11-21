#!/usr/bin/env python

import numpy as np

def read_file(input_file):
    data = np.fromfile(file=open(input_file), dtype=float, sep=" ")
    n = int(len(data)/7)
    data = data.reshape((n, 7))

    return data, n
