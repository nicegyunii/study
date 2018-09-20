'''
Created on 2018/09/07

@author: user36-pci
'''
print("import_test.py is imported !")

def print_name():
    print(__name__)

age = 20
name = "gyuni"

print("{0} was {1} uears old when he wrote this book ".format(name, age).capitalize())


def func(a, b=5, c=10):
 print ('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)
func(c=50)