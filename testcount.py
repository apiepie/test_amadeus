#!/usr/bin/python
# vim: set fileencoding=utf-8 :


import os
import sys
import getopt
import gzip
import bz2
import csv, codecs
import itertools
import operator

def count_lines2(file_name):
    fd = bz2.BZ2File(file_name, 'rb')
    c = codecs.iterdecode(fd, "utf-8")
    n = 0
    reader = csv.reader(c, delimiter='^')

    for line in reader:
        n +=1
    fd.close()
    return n




print(count_lines2(r'C:\Users\piepie\Downloads\searches.csv.bz2'))
print(count_lines2(r'C:\Users\piepie\Downloads\bookings.csv.bz2'))