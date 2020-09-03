from tkinter import *
import tkinter as tk

import tkinterChallenge_func


class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__(self)

        self.master = master
        self.master.minsize(500,170)
        self.master.maxsize(500,170)
        self.master.title('Check files')
        self.master.columnconfigure(1,weight=1)


        self.btn_browse = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: tkinterChallenge_func.browse1(self))
        self.btn_browse.grid(row=1, column=0, padx=(10,0), pady=(35,0), sticky=W)
        self.btn_browse2 = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: tkinterChallenge_func.browse2(self))
        self.btn_browse2.grid(row=2, column=0, padx=(10,0), pady=(10,0), sticky=W)
        self.btn_checkFiles = tk.Button(self.master, width=12, height=2, text='Check for files...', command=lambda: tkinterChallenge_func.fileTranster(self))
        self.btn_checkFiles.grid(row=3, column=0, padx=(10,0), pady=(10,0), sticky=W)
        self.btn_closeProgram = tk.Button(self.master, width=12, height=2, text='Close Program', command=lambda: tkinterChallenge_func.closeProgram(self))
        self.btn_closeProgram.grid(row=3, column=3, padx=(10,10), pady=(10,0), sticky=E)

        self.txt_browse = tk.Entry(self.master, text='')
        self.txt_browse.grid(row=1, column=1, rowspan=1, columnspan=3, padx=(10,10), pady=(35,0), stick=W+E)
        self.txt_browse2 = tk.Entry(self.master, text='')
        self.txt_browse2.grid(row=2, column=1, rowspan=1, columnspan=3, padx=(10,10), pady=(10,0), stick=W+E)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
