#!/usr/bin/python3

from ctypes import c_int

class alx_listint_t:
    pass

alx_listint_t.n = c_int()
alx_listint_t.next = None

def print_list_integer(my_list=[]):
    for num in my_list:
        if isinstance(num, int):
            alx_listint_t.n = num
            print("{:d}".format(alx_listint_t.n))
