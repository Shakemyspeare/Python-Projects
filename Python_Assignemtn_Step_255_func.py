import os.path,time
from tkinter import *
import tkinter as tk
import shutil

import tkinterChallenge_main

def browse1(self):
    from tkinter import filedialog
    folder1 = filedialog.askdirectory(initialdir = "/",title = "Please select a folder", mustexist=True)
    self.txt_browse.delete(0,END)
    self.txt_browse.insert(0,folder1)

def browse2(self):
    from tkinter import filedialog
    folder2 = filedialog.askdirectory(initialdir = "/",title = "Please select a folder", mustexist=True)
    self.txt_browse2.delete(0,END)
    self.txt_browse2.insert(0,folder2)

def fileTranster(self):
    source = self.txt_browse.get()
    destination = self.txt_browse2.get()
    files = os.listdir(source)
    for filename in files:
        if(time.time() - os.path.getmtime(os.path.join(source,filename))) / 3600 < 24*1:
            shutil.move(os.path.join(source,filename), destination)
    
def closeProgram(self):
    self.master.destroy()
    os._exit(0)
