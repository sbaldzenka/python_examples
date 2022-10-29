from ctypes import *

libc = cdll.LoadLibrary('./libc_functions.so')

libc.call_sum_func()