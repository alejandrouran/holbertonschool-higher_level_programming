#!/usr/bin/env python3
def no_c(my_string):
    characters = "cC"
    my_string = ''.join( i for i in my_string if i not in characters)
    return my_string
