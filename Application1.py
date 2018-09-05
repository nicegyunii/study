'''
Created on 2018/09/05

@author: user36-pci
'''

import tkinter

class Application(tkinter.Frame):
    '''
    classdocs
    '''


    def __init__(self, master=None):
        '''
        Constructor
        '''
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "hello!!!"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tkinter.Button(self, text="QUIT", command=self.master.destroy)
        self.quit.pack(side="bottom")


    def say_hi(self):
        print("hi there!!")


root = tkinter.Tk()
root.geometry("400x300")
app = Application(master=root)
app.mainloop()