#!/usr/bin/env python3
def no_c(my_string):
    n_str = ''.join(i for i in my_string if i != "c" and i != "C")
    return(n_str)

