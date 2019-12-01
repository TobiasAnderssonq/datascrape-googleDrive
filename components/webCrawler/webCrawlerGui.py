from Tkinter import *
import webCrawler

class webCrawlerGui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.crawler_frame = Frame(parent, bg='#80c1ff', bd=5)
        self.crawler_frame.place(relx=0.55, rely=0, relwidth=0.9, relheight=0.1, anchor='n')
        
        self.startCrawlerButton = Button(self.crawler_frame, text="START CRAWLING", command=self.startCrawler)
        self.startCrawlerButton.place(relx=0.7, relheight=1, relwidth=0.3)
    
        self.startingUrlInput = Entry(self.crawler_frame, font=40)
        self.startingUrlInput.place(relwidth=0.65, relheight=1)
        self.startingUrlInput.insert(0,"https://en.wikipedia.org/wiki/Wikipedia:Random")

    def startCrawler(self):
        crawler = webCrawler.PyCrawler()
        textInput = self.startingUrlInput.get()
        crawler.start(textInput)

