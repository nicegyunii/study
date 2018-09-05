'''
Created on 2018/09/05

@author: user36-pci
'''

import tkinter

tkinter.Widget = tkinter.Label(None,text='xxxxx')
tkinter.Widget.pack()

if __name__ == '__main__':
    print('hello egg!!!')

family = ['mother', 'father', 'gentleman', 'sexy lady']

print(len(family))


print(family[0])

for x in family:
    print(x)