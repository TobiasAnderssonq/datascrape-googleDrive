from tkinter import *
import sys
import nordnet_datascrape as datascrape 
import pandas as pd
import components.datascrapeTable.datascrapeGui
import components.webCrawler.webCrawlerGui
import components.sideMenu.sideMenu

class TestApp(Frame):
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('1000x800+200+100') # Set Window size
            self.main.title('Table app')
            root = Frame(self.main)
            root.pack(fill="both",expand=True)
            root.grid_columnconfigure(0,weight=1)
            root.grid_rowconfigure(0,weight=1)
            self.current_frame = None

            self.canvas = Frame(root, bg='cyan')
            self.canvas.grid(row=0, column=0)
            self.canvas.pack(fill="both",expand=1)

            sideMenu = components.sideMenu.sideMenu.sideMenu(root, self)
            sideMenu.grid(row=0,column=1)
            
            self.show_frame(components.webCrawler.webCrawlerGui.webCrawlerGui)

        def show_frame(self, page_name):
            if self.current_frame is not None:
                self.current_frame.destroy()
            self.current_frame = page_name(self.canvas)
            self.current_frame.pack(fill="both", expand=1)

app = TestApp()
app.mainloop()            