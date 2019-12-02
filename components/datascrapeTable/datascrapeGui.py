from Tkinter import *
import pandas as pd
import sys
from pandastable import Table, TableModel
sys.path.insert(1, '../../')
import nordnet_datascrape as datascrape


class datascrapeTable(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.upper_frame = Frame(parent, bg='#80c1ff', bd=5)
        self.upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        self.lower_frame = Frame(parent, bg='#80c1ff', bd=10)
        self.lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        self.entry = Entry(self.upper_frame, font=40)
        self.entry.place(relwidth=0.65, relheight=1)

        self.button = Button(self.upper_frame, text="Get Nordnet Data", font=40, command = self.handleButtonClick)
        self.button.place(relx=0.7, relheight=1, relwidth=0.3)

        df = None
        self.table = pt = Table(self.lower_frame, dataframe=df, showtoolbar=True, showstatusbar=True)
        pt.show()

    def handleButtonClick(self):
            df = datascrape.runDatascrape()
            self.table.model.df = df
            self.table.redraw()
            print df    
