#!/usr/bin/env python

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
def display(T):
    print "{0:.1f}".format(T)

t = raw_input('temp (nnF or nnC)')

if t.endswith('F'):
    display(celsius(int(t[:-1])))
else:
    display(fahrenheit(int(t[:-1])))
