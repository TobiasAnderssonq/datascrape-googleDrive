from tkinter import *
import nordnet_datascrape as datascrape
from pandastable import Table, TableModel
import pandas as pd

class TestApp(Frame):
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('1000x800+200+100') # Set Window size
            self.main.title('Table app')
            root = Frame(self.main)
            root.pack(fill=BOTH,expand=1)    

            upper_frame = Frame(root, bg='#80c1ff', bd=5)
            upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

            lower_frame = Frame(root, bg='#80c1ff', bd=10)
            lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

            entry = Entry(upper_frame, font=40)
            entry.place(relwidth=0.65, relheight=1)

            button = Button(upper_frame, text="Get Nordnet Data", font=40, command = self.handleButtonClick)
            button.place(relx=0.7, relheight=1, relwidth=0.3)

            df = None
            self.table = pt = Table(lower_frame, dataframe=df,
                                    showtoolbar=True, showstatusbar=True)
            pt.show()                        
            return

        def handleButtonClick(self):
            df = datascrape.runDatascrape()
            self.table.model.df = df
            self.table.redraw()
            print df


app = TestApp()
app.mainloop()            