'''
Created on 2018/09/05

@author: user36-pci
'''
import sys
import tkinter
from cgitb import text
from Tools.demo.sortvisu import WIDTH

root = tkinter.Tk()

root.title(u"Software Title")
root.geometry("400x300")


def DeleteEntryValue(event):
    print(editBox.get())
    editBox.delete(0, tkinter.END)


#ラベル
Static1 = tkinter.Label(text=u"test labdl", foreground='#ff0000', background='#ffaacc')
Static1.place(x=50, y=100)

editBox = tkinter.Entry(width=40)
editBox.insert(tkinter.END, "挿入する文字列")
editBox.pack()


button = tkinter.Button(text="push!!")
button.bind("<Button-1>", DeleteEntryValue)
button.pack()


root.mainloop()