#!/usr/bin/env python

'''
Project Name: Janggut Touch App
Project Description: Read CSV/EXCEL files -- plot a graph -- with GUI (Simple; Tkinter)
'''

'''
TKINTER -- Python's de-facto standard GUI (Graphical User Interface) package
'''
# try:
# Python 2
from Tkinter import *
from tkFileDialog import askopenfilename
import ttk
# except ImportError:
#     # Python 3
#     from tkinter import *
#     from tkinter.filedialog import askopenfilename
#     import tkinter.ttk as ttk

'''
PANDAS -- data structures and data analysis tools
'''
import pandas as pd

'''
Matplotlib -- Python 2D plotting library
'''
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

'''
NumPy -- fundamental package for scientific computing with Python
'''
import numpy as np

'''
Here, we are creating our class, Window, and inheriting from the Frame
class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
'''
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        '''
        Initialization for some parameters
        '''
        self.xlabelName = "N/A"
        self.ylabelName = "N/A"

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the geometry, title, and etc of our master widget
        self.master.geometry("757x1037+832+67")
        self.master.title("Janggut Touch App (Dev:0.0.1)")
        self.master.configure(background="#d9d9d9")
        self.master.configure(highlightbackground="#d9d9d9")
        self.master.configure(highlightcolor="black")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        '''
        UPLOAD FILE (LABELFRAME)
        '''
        self.labelFrame = LabelFrame(self.master)
        self.labelFrame.place(relx=0.05, rely=0.01, relheight=0.10, relwidth=0.9)
        self.labelFrame.configure(relief=GROOVE)
        # self.labelFrame.configure(activebackground="#f9f9f9")
        # self.labelFrame.configure(activeforeground="black")
        self.labelFrame.configure(background="#d9d9d9")#
        # self.labelFrame.configure(disabledforeground="#a3a3a3")
        self.labelFrame.configure(foreground="#000000")#
        # self.labelFrame.configure(highlightbackground="#d9d9d9")
        # self.labelFrame.configure(highlightcolor="black")
        self.labelFrame.configure(text='''Upload File:''')#
        self.labelFrame.configure(width=800)#

        '''
        BROWSE (BUTTON)
        '''
        self.button = Button(self.labelFrame)
        self.button.place(relx=0.03, rely=0.06, relheight=0.7, relwidth=0.2)
        self.button.configure(activebackground="#d9d9d9")
        self.button.configure(activeforeground="#000000")
        self.button.configure(background="#d9d9d9")
        self.button.configure(disabledforeground="#a3a3a3")
        self.button.configure(foreground="#000000")
        self.button.configure(highlightbackground="#d9d9d9")
        self.button.configure(highlightcolor="black")
        self.button.configure(pady="0")
        self.button.configure(text='''Browse''')
        self.button.configure(width=122)
        self.button.configure(command=self.load)

        '''
        DATAFRAME (TEXTBOX)
        '''
        self.text = Text(self.labelFrame)
        self.text.place(relx=0.25, rely=0.06, relheight=0.7, relwidth=0.72)
        self.text.configure(background="white")
        self.text.configure(font="TkTextFont")
        self.text.configure(foreground="black")
        self.text.configure(highlightbackground="#d9d9d9")
        self.text.configure(highlightcolor="black")
        self.text.configure(insertbackground="black")
        self.text.configure(selectbackground="#c4c4c4")
        self.text.configure(selectforeground="black")
        self.text.configure(width=500)
        # self.text.configure(wrap=WORD)

        '''
        DATAFRAME (LABELRAME)
        '''
        self.labelFrame1 = LabelFrame(self.master)
        self.labelFrame1.place(relx=0.05, rely=0.12, relheight=0.2, relwidth=0.9)
        self.labelFrame1.configure(relief=GROOVE)
        self.labelFrame1.configure(background="#d9d9d9")
        # self.labelFrame1.configure(disabledforeground="#a3a3a3")
        self.labelFrame1.configure(foreground="#000000")
        self.labelFrame1.configure(text='''Data Frame :''')
        self.labelFrame.configure(width=800)#

        '''
        DATAFRAME (TEXTBOX)
        '''
        self.text1 = Text(self.labelFrame1)
        self.text1.place(relx=0.01, rely=0.01, relheight=0.95, relwidth=0.98)
        self.text1.configure(background="white")
        self.text1.configure(font="TkTextFont")
        self.text1.configure(foreground="black")
        self.text1.configure(highlightbackground="#d9d9d9")
        self.text1.configure(highlightcolor="black")
        self.text1.configure(insertbackground="black")
        self.text1.configure(selectbackground="#c4c4c4")
        self.text1.configure(selectforeground="black")
        self.text1.configure(width=684)
        # self.text.configure(wrap=WORD)

        '''
        LABELFRAME (LABELRAME)
        '''
        self.labelFrame2 = LabelFrame(self.master)
        self.labelFrame2.place(relx=0.05, rely=0.33, relheight=0.12, relwidth=0.44)
        self.labelFrame2.configure(relief=GROOVE)
        self.labelFrame2.configure(foreground="black")
        self.labelFrame2.configure(text='''LabelFrame''')
        self.labelFrame2.configure(background="#d9d9d9")
        self.labelFrame2.configure(width=340)

        '''
        X-AXIS (LABEL)
        '''
        self.label1 = Label(self.labelFrame2)
        self.label1.place(relx=0.00, rely=0.05, height=31, width=67)
        self.label1.configure(background="#d9d9d9")
        self.label1.configure(disabledforeground="#a3a3a3")
        self.label1.configure(foreground="#000000")
        self.label1.configure(text='''X-axis :''')

        '''
        Y-AXIS (LABEL)
        '''
        self.label2 = Label(self.labelFrame2)
        self.label2.place(relx=0.00, rely=0.5, height=31, width=66)
        self.label2.configure(background="#d9d9d9")
        self.label2.configure(disabledforeground="#a3a3a3")
        self.label2.configure(foreground="#000000")
        self.label2.configure(text='''Y-axis :''')

        '''
        MIN (LABEL)
        '''
        self.label3 = Label(self.labelFrame2)
        self.label3.place(relx=0.47, rely=0.05, height=31, width=67)
        self.label3.configure(background="#d9d9d9")
        self.label3.configure(disabledforeground="#a3a3a3")
        self.label3.configure(foreground="#000000")
        self.label3.configure(text='''MIN :''')

        '''
        MAX (LABEL)
        '''
        self.label4 = Label(self.labelFrame2)
        self.label4.place(relx=0.47, rely=0.5, height=31, width=66)
        self.label4.configure(background="#d9d9d9")
        self.label4.configure(disabledforeground="#a3a3a3")
        self.label4.configure(foreground="#000000")
        self.label4.configure(text='''MAX :''')

        '''
        X-AXIS (OPTION MENU)
        '''
        self.variableX = StringVar(self.labelFrame2)
        self.variableX.set("") # default value

        self.entry1 = OptionMenu(self.labelFrame2, self.variableX, "")
        self.entry1.place(relx=0.2, rely=0.05, relheight=0.4, relwidth=0.3)
        self.entry1.configure(background="white")
        self.entry1.configure(disabledforeground="#a3a3a3")
        self.entry1.configure(font="TkFixedFont")
        self.entry1.configure(foreground="#000000")
        # self.entry1.configure(insertbackground="black")
        self.entry1.configure(width=100)

        '''
        Y-AXIS (OPTION MENU)
        '''
        self.variableY = StringVar(self.labelFrame2)
        self.variableY.set("") # default value

        self.entry2 = OptionMenu(self.labelFrame2, self.variableY, "")
        self.entry2.place(relx=0.2, rely=0.5, relheight=0.4, relwidth=0.3)
        self.entry2.configure(background="white")
        self.entry2.configure(disabledforeground="#a3a3a3")
        self.entry2.configure(font="TkFixedFont")
        self.entry2.configure(foreground="#000000")
        # self.entry2.configure(insertbackground="black")
        self.entry2.configure(width=100)

        '''
        MIN (TEXTBOX)
        '''
        self.entry3 = Entry(self.labelFrame2)
        self.entry3.place(relx=0.65, rely=0.05, relheight=0.4, relwidth=0.3)
        self.entry3.configure(background="white")
        self.entry3.configure(font="TkTextFont")
        self.entry3.configure(foreground="black")
        self.entry3.configure(highlightbackground="#d9d9d9")
        self.entry3.configure(highlightcolor="black")
        self.entry3.configure(insertbackground="black")
        self.entry3.configure(selectbackground="#c4c4c4")
        self.entry3.configure(selectforeground="black")
        # self.entry3.configure(insertbackground="black")
        self.entry3.configure(width=100)

        '''
        MAX (TEXTBOX)
        '''
        self.entry4 = Entry(self.labelFrame2)
        self.entry4.place(relx=0.65, rely=0.5, relheight=0.4, relwidth=0.3)
        self.entry4.configure(background="white")
        self.entry4.configure(font="TkTextFont")
        self.entry4.configure(foreground="black")
        self.entry4.configure(highlightbackground="#d9d9d9")
        self.entry4.configure(highlightcolor="black")
        self.entry4.configure(insertbackground="black")
        self.entry4.configure(selectbackground="#c4c4c4")
        self.entry4.configure(selectforeground="black")
        # self.entry4.configure(insertbackground="black")
        self.entry4.configure(width=100)

        '''
        TYPE OF GRAPH (LABELFRAME)
        '''
        self.labelFrame3 = LabelFrame(self.master)
        self.labelFrame3.place(relx=0.5, rely=0.33, relheight=0.12, relwidth=0.45)
        self.labelFrame3.configure(relief=GROOVE)
        self.labelFrame3.configure(foreground="black")
        self.labelFrame3.configure(text='''Type of Graph''')
        self.labelFrame3.configure(background="#d9d9d9")
        self.labelFrame3.configure(highlightbackground="#d9d9d9")
        self.labelFrame3.configure(highlightcolor="black")
        self.labelFrame3.configure(width=340)

        self.var = StringVar(self.labelFrame3)

        '''
        BAR CHART (RADIOBUTTON)
        '''
        self.radioButton1 = Radiobutton(self.labelFrame3, variable=self.var, value="bar", command=self.sel)
        self.radioButton1.place(relx=0.00, rely=0.10, relheight=0.2, relwidth=0.31)
        self.radioButton1.configure(activebackground="#d9d9d9")
        self.radioButton1.configure(activeforeground="#000000")
        self.radioButton1.configure(background="#d9d9d9")
        self.radioButton1.configure(disabledforeground="#a3a3a3")
        self.radioButton1.configure(foreground="#000000")
        self.radioButton1.configure(highlightbackground="#d9d9d9")
        self.radioButton1.configure(highlightcolor="black")
        # self.radioButton1.configure(justify=LEFT)
        self.radioButton1.configure(text='''Bar Chart''')

        '''
        HISTOGRAM (RADIOBUTTON)
        '''
        self.radioButton2 = Radiobutton(self.labelFrame3, variable=self.var, value="hist", command=self.sel)
        self.radioButton2.place(relx=0.3, rely=0.10, relheight=0.2, relwidth=0.35)
        self.radioButton2.configure(activebackground="#d9d9d9")
        self.radioButton2.configure(activeforeground="#000000")
        self.radioButton2.configure(background="#d9d9d9")
        self.radioButton2.configure(disabledforeground="#a3a3a3")
        self.radioButton2.configure(foreground="#000000")
        self.radioButton2.configure(highlightbackground="#d9d9d9")
        self.radioButton2.configure(highlightcolor="black")
        # self.radioButton2.configure(justify=LEFT)
        self.radioButton2.configure(text='''Histogram''')

        '''
        SCATTER PLOT (RADIOBUTTON)
        '''
        self.radioButton3 = Radiobutton(self.labelFrame3, variable=self.var, value="scatter", command=self.sel)
        self.radioButton3.place(relx=0.6, rely=0.10, relheight=0.2, relwidth=0.37)
        self.radioButton3.configure(activebackground="#d9d9d9")
        self.radioButton3.configure(activeforeground="#000000")
        self.radioButton3.configure(background="#d9d9d9")
        self.radioButton3.configure(disabledforeground="#a3a3a3")
        self.radioButton3.configure(foreground="#000000")
        self.radioButton3.configure(highlightbackground="#d9d9d9")
        self.radioButton3.configure(highlightcolor="black")
        # self.radioButton3.configure(justify=LEFT)
        self.radioButton3.configure(text='''Scatter Plot''')

        '''
        GENERATE GRAPH (BUTTON)
        '''
        self.button2 = Button(self.labelFrame3, command=self.plot)
        self.button2.place(relx=0.3, rely=0.4, height=35, width=138)
        self.button2.configure(activebackground="#d9d9d9")
        self.button2.configure(activeforeground="#000000")
        self.button2.configure(background="#d9d9d9")
        self.button2.configure(disabledforeground="#a3a3a3")
        self.button2.configure(foreground="#000000")
        self.button2.configure(highlightbackground="#d9d9d9")
        self.button2.configure(highlightcolor="black")
        self.button2.configure(pady="0")
        self.button2.configure(text='''Generate Graph''')

        '''
        GENERATED GRAPGH (LABELRAME)
        '''
        self.labelFrame4 = LabelFrame(self.master)
        self.labelFrame4.place(relx=0.05, rely=0.45, relheight=0.5, relwidth=0.9)
        self.labelFrame4.configure(relief=GROOVE)
        self.labelFrame4.configure(foreground="black")
        self.labelFrame4.configure(text='''Graph''')
        self.labelFrame4.configure(background="#d9d9d9")
        self.labelFrame4.configure(width=340)

        '''
        GRAPH (MATPLOTLIB)
        '''
        self.f = Figure(figsize=(1,1), dpi=80)
        self.a = self.f.add_subplot(111)
        # self.a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        # self.a.set_xlabel('xlabel')
        # self.a.set_ylabel('ylabel')
        # self.a.xaxis.set_visible(True)
        # self.a.yaxis.set_visible(True)

        # fig=plt.figure(figsize=(8,8))
        # ax=fig.add_axes([0.1,0.1,0.8,0.8],polar=True)
        # canvas=FigureCanvasTkAgg(fig,master=root)
        # canvas.get_tk_widget().grid(row=0,column=1)
        # canvas.draw()

        self.canvas = FigureCanvasTkAgg(self.f, self.labelFrame4)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.labelFrame4)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

        '''
        DISCLAIMER
        '''
        self.label5 = Label(self.master)
        self.label5.place(relx=0.4, rely=0.96)
        self.label5.configure(background="#d9d9d9")
        self.label5.configure(disabledforeground="#a3a3a3")
        self.label5.configure(foreground="#000000")
        self.label5.configure(text='''--- Software under development ---''')

    '''
    Load a selected filetypes
    '''
    def load(self):
        self.name = askopenfilename(filetypes=[('CSV', '*.csv',), ('Excel', ('*.xls', '*.xlsx'))])

        if self.name:
            if self.name.endswith('.csv'):
                self.df = pd.read_csv(self.name)
            else:
                self.df = pd.read_excel(self.name)

            self.filename = self.name

            # self.variableX.set(list(self.df)[0])
            self.optionList = list(self.df)

            self.intList = list(range(len(self.df)))
            # print(self.intList)

            # self.variableX = StringVar(self.labelFrame2)
            # self.variableX.set(list(self.df)[0])
            # print(self.options)

            '''
            X-AXIS (OPTION MENU)
            '''
            self.variableX = StringVar(self.labelFrame2)
            self.variableX.set("")  # default choice

            self.entry1 = OptionMenu(self.labelFrame2, self.variableX, *self.optionList, command=self.funcX)
            self.entry1.place(relx=0.2, rely=0.05, relheight=0.4, relwidth=0.3)
            self.entry1.configure(background="white")
            self.entry1.configure(disabledforeground="#a3a3a3")
            self.entry1.configure(font="TkFixedFont")
            self.entry1.configure(foreground="#000000")
            # self.entry1.configure(insertbackground="black")
            self.entry1.configure(width=100)

            '''
            Y-AXIS (OPTION MENU)
            '''
            self.variableY = StringVar(self.labelFrame2)
            self.variableY.set("") # default value

            self.entry2 = OptionMenu(self.labelFrame2, self.variableY, *self.optionList, command=self.funcY)
            self.entry2.place(relx=0.2, rely=0.5, relheight=0.4, relwidth=0.3)
            self.entry2.configure(background="white")
            self.entry2.configure(disabledforeground="#a3a3a3")
            self.entry2.configure(font="TkFixedFont")
            self.entry2.configure(foreground="#000000")
            # self.entry2.configure(insertbackground="black")
            self.entry2.configure(width=100)

            self.display()

    '''
    Display selected files data
    '''
    def display(self):
        # ask for file if not loaded yet
        if self.df is None:
            self.load()

        # display if loaded
        if self.df is not None:
            self.text.delete('1.0', END)
            self.text.insert('end', self.filename + '\n')

            # self.text.insert('end', str(self.df.head()) + '\n')
            self.text1.delete('1.0', END)
            self.text1.insert('end', str(self.df) + '\n')

    '''
    Exit program
    '''
    def client_exit(self):
        exit()

    '''
    Getting the Label Name (X-AXIS)
    '''
    def funcX(self, value):
        # selection = "xLabel: " + str(value)
        # print(selection)
        # self.a.set_xlabel(value)
        # # self.a.set_ylabel('ylabel')

        self.xlabelName = value

        self.refreshLabel()

    '''
    Getting the Label Name (Y-AXIS)
    '''
    def funcY(self, value):
        # selection = "yLabel: " + str(value)
        # print(selection)
        # # self.a.set_xlabel('xlabel')
        # self.a.clear()
        # self.a.set_ylabel(value)

        self.ylabelName = value

        self.refreshLabel()

    '''
    Getting the Label Name (X-AXIS)
    '''
    def funcMin(self, value):
        # selection = "xLabel: " + str(value)
        # print(selection)
        # self.a.set_xlabel(value)
        # # self.a.set_ylabel('ylabel')

        self.minVal = value

        # self.refreshLabel()

    '''
    Getting the Label Name (Y-AXIS)
    '''
    def funcMax(self, value):
        # selection = "yLabel: " + str(value)
        # print(selection)
        # # self.a.set_xlabel('xlabel')
        # self.a.clear()
        # self.a.set_ylabel(value)

        self.maxVal = value

        # self.refreshLabel()

    '''
    Refresh the Label (X and Y)
    '''
    def refreshLabel(self):
        self.a.clear()         # clear axes from previous plot

        self.a.set_xlabel(self.xlabelName)
        self.a.set_ylabel(self.ylabelName)
        self.a.title.set_text(self.xlabelName + " VS " + self.ylabelName)
        self.canvas.draw()

    '''
    Graph type selection
    '''
    # TODO:
    def sel(self):
        # selection = "Graph Type: " + str(self.var.get())
        # print(selection)
        self.graphType = str(self.var.get())

        # self.plot()

    def plot(self):
        c = ['r','b','g']  # plot marker colors
        self.a.clear()         # clear axes from previous plot

        if self.graphType == 'bar':
            # TODO:
            theta = self.df[self.xlabelName][int(self.entry3.get()):int(self.entry4.get())]
            r = self.df[self.ylabelName][int(self.entry3.get()):int(self.entry4.get())]
            self.a.bar(theta, r, align='center', alpha=0.1)
        else:
            theta = np.random.uniform(0,360,10)
            r = np.random.uniform(0,1,10)
            self.a.plot(theta,r,linestyle="None",marker='o', color='r', markersize='10', markerfacecolor='b', markeredgewidth='2', markeredgecolor='orange')

        self.a.set_xlabel(self.xlabelName)
        self.a.set_ylabel(self.ylabelName)
        self.a.title.set_text(self.xlabelName + " VS " + self.ylabelName)
        self.canvas.draw()



# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)

#mainloop
# root.update()
root.mainloop()
