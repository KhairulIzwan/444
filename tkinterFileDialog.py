#!/usr/bin/env python3

from tkinter import filedialog
from tkinter import *

root = Tk()

# askopenfilename
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg")("all files","*.*")))
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
print (root.filename)

# asksaveasfilename
# root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file")
print (root.filename)

# askdirectory
root.directory = filedialog.askdirectory()
print (root.directory)
