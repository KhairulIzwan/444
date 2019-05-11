#!/usr/bin/env python

import sys

try:
    # Python 2
    from Tkinter import *
    from tkFileDialog import askopenfilename
    import ttk
except ImportError:
    # Python 3
    from tkinter import *
    from tkinter.filedialog import askopenfilename
    import tkinter.ttk as ttk

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None

class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self._bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        self._fgcolor = '#000000'  # X11 color: 'black'
        self._compcolor = '#d9d9d9' # X11 color: 'gray85'
        self._ana1color = '#d9d9d9' # X11 color: 'gray85'
        self._ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("757x1037+832+67")
        top.title("New Toplevel 1")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.04, rely=0.58, relheight=0.4, relwidth=0.92)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=695)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.75, rely=0.52, height=42, width=138)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Generate Graph''')

        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.05, rely=0.39, relheight=0.18
                , relwidth=0.44)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Type of Graph''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=330)

        self.Radiobutton1 = Radiobutton(self.Labelframe1)
        self.Radiobutton1.place(relx=0.06, rely=0.22, relheight=0.2
                , relwidth=0.31)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(text='''Bar Chart''')

        self.Radiobutton2 = Radiobutton(self.Labelframe1)
        self.Radiobutton2.place(relx=0.06, rely=0.38, relheight=0.2
                , relwidth=0.35)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''Histogram''')

        self.Radiobutton3 = Radiobutton(self.Labelframe1)
        self.Radiobutton3.place(relx=0.06, rely=0.54, relheight=0.2
                , relwidth=0.37)
        self.Radiobutton3.configure(activebackground="#d9d9d9")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#d9d9d9")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify=LEFT)
        self.Radiobutton3.configure(text='''Scatter Plot''')

        self.Button3 = Button(top)
        self.Button3.place(relx=0.28, rely=0.05, height=52, width=122)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Browse''')
        self.Button3.configure(width=122)
        self.Button3.configure(command=askopenfilename)

        self.Label5 = Label(top)
        self.Label5.place(relx=0.03, rely=0.06, height=31, width=147)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Upload File:''')
        self.Label5.configure(width=147)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.05, rely=0.13, height=31, width=111)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Data Frame :''')

        self.Text1 = Text(top)
        self.Text1.place(relx=0.05, rely=0.16, relheight=0.21, relwidth=0.9)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=684)
        self.Text1.configure(wrap=WORD)

        self.Labelframe2 = LabelFrame(top)
        self.Labelframe2.place(relx=0.5, rely=0.39, relheight=0.12
                , relwidth=0.45)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Labelframe''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(width=340)

        self.Label1 = Label(self.Labelframe2)
        self.Label1.place(relx=0.03, rely=0.24, height=31, width=67)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''X-axis :''')

        self.Label2 = Label(self.Labelframe2)
        self.Label2.place(relx=0.03, rely=0.56, height=31, width=66)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Y-axis :''')

        self.Entry1 = Entry(self.Labelframe2)
        self.Entry1.place(relx=0.24, rely=0.24, relheight=0.29, relwidth=0.72)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=244)

        self.Entry2 = Entry(self.Labelframe2)
        self.Entry2.place(relx=0.24, rely=0.56, relheight=0.29, relwidth=0.72)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=244)

if __name__ == '__main__':
    vp_start_gui()
