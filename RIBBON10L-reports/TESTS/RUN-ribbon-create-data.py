#! /usr/bin/env python3.8

"""
# File: RUN-ribbon-create-data.py
# Date: Wed 07 Jun 2023 03:33:10 PM +08

DESCRIPTION

# NOTE 1: numpy version conflict for python3.9, use python3.8 OK
# NOTE 2: Python does not have a switch statement functionality.
#
"""
import numpy as np
from datetime import datetime

# =========================================================
# MAIN PROGRAM
# =========================================================
print("Bismillah Hirrahma Nirrahim WRY \n")

## OUTPUT FILE
## OUTFILE  = input("Enter  output filename.txt: \t")
## output_file_HDL.write(line-to-write xxx)

OUTFILE = "data-output-ribbon.txt"
OUTPUT_FILE_HDL = open(OUTFILE,'w')

"""
DEFINE RANGES OF FLOATS
REF: https://pynative.com/python-range-for-float-numbers/
NumPy has the arange() function to get the range of floating-point numbers.
Use NumPy’s arange() and linspace() functions to use decimal numbers in 
a start, stop and step argument to produce a range of floating-point numbers.
"""

the_now  = datetime.now() 
the_date = the_now.strftime("%Y-%m-%d")
the_time = the_now.strftime("%H:%M:%S")

line_str_A1 = "#  Date : " + the_date + "\n"
line_str_A2 = "#  Time : " + the_time + " MYT (+8 UTC)\n"
line_str_A3 = "#  Code : RUN-ribbon-create-data.py \n"
line_str_A4 = "#  Output : " + OUTFILE + "\n"

## =========================================================
## WRITE TO OUTPUT FILE  
OUTPUT_FILE_HDL.write("#  Bismillah Hirrahma Nirrahim \n")
OUTPUT_FILE_HDL.write(line_str_A1)
OUTPUT_FILE_HDL.write(line_str_A2)
OUTPUT_FILE_HDL.write(line_str_A3)
OUTPUT_FILE_HDL.write(line_str_A4)


def fxn_x(t):
    x_val = (t*t)
    return x_val
     
def fxn_y(t):    
    y_val = (t*t*t) - 3*t + 3
    return y_val
 
## START THE FOR LOOP (GOOD RANGE)
## TO MAKE LINEAR TRANSFORMATION u = 0.00 AT t = -2.00 
##                               u = 1.00 AT t = +2.00


## EXECUTE START THE FOR LOOP (GOOD RANGE)
for t in np.arange(-2.0, +2.001, 0.001):   

    x = fxn_x(t)
    y = fxn_y(t)
    
    print("t = ", t, " x(", t, ") = ", x, " y(", t, ") = ", y ) 
    
    ## WRITE TO FILE
    line_str_to_write = "\t" + str(t) + "\t" + str(x) + "\t" + str(y) + "\n"
    OUTPUT_FILE_HDL.write(line_str_to_write)

## END THE FOR LOOP
OUTPUT_FILE_HDL.write("#  Alhamdulillah Hirrabil Alamin \n")

## INPUT_FILE_HDL.close()
OUTPUT_FILE_HDL.close()

print("\nAlhamdulillah Hirrabil Alamin WRY \n")  
## ========================================================

"""
wruslan@HPLaptop-01-ub20:~/opt/wks-pydev/ribbon-create-datafile$ python3 RUN-ribbon-create-data.py 
Bismillah Hirrahma Nirrahim WRY 

t =  -5.0  x( -5.0 ) =  25.0  y( -5.0 ) =  -107.0
t =  -4.0  x( -4.0 ) =  16.0  y( -4.0 ) =  -49.0
t =  -3.0  x( -3.0 ) =  9.0  y( -3.0 ) =  -15.0
t =  -2.0  x( -2.0 ) =  4.0  y( -2.0 ) =  1.0
t =  -1.0  x( -1.0 ) =  1.0  y( -1.0 ) =  5.0
t =  0.0  x( 0.0 ) =  0.0  y( 0.0 ) =  3.0
t =  1.0  x( 1.0 ) =  1.0  y( 1.0 ) =  1.0
t =  2.0  x( 2.0 ) =  4.0  y( 2.0 ) =  5.0
t =  3.0  x( 3.0 ) =  9.0  y( 3.0 ) =  21.0
t =  4.0  x( 4.0 ) =  16.0  y( 4.0 ) =  55.0
t =  5.0  x( 5.0 ) =  25.0  y( 5.0 ) =  113.0

Alhamdulillah Hirrabil Alamin WRY 

wruslan@HPLaptop-01-ub20:~/opt/wks-pydev/ribbon-create-datafile$ 
"""



