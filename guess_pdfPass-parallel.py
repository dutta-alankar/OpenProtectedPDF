# -*- coding: utf-8 -*-
"""
Created on Sun Jun  16 21:57:11 2024
@author: alankar
Usage: time mpiexec -n <num_procs> python guess_pdfPass-parallel.py
Dependency: qpdf (https://github.com/qpdf/qpdf), tested with version 11.9.1
Note: Make sure qpdf and its libraries are added to PATH and LD_LIBRARY_PATH respectively
Thanks: Samriddhi Sankar Maity
- This code uses MPI to perform coordinated parallel guesses using multiple processors.
- This is ideal for guessing long passwords with brute force using supercomputers
"""

import subprocess as sp
from mpi4py import MPI
from itertools import product

## start parallel programming ---------------------------------------- #
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

verbose = False

initial_known_pass = "9899"

input_file = "sample.pdf"
output_file = "sample-decrypt.pdf"

# trying to guess unknown 6 digits
tries = list(product(range(10),range(10),range(10),range(10),range(10),range(10)))

for i in range(rank, len(tries), size):
    guess_pass = "".join(str(x) for x in tries[i])
    text = sp.getoutput(f'qpdf -password="{initial_known_pass}{guess_pass}" -decrypt {input_file} {output_file}')
    if verbose:
        print(f"{initial_known_pass}{guess_pass}: {text}", flush=True)
    if "invalid password" not in text:
        print(f"Password found: {initial_known_pass}{guess_pass}", flush=True)
        comm.Abort()
print("Set settings failed to guess the password.")
