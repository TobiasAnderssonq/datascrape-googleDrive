from Tkinter import *
import components.datascrapeTable.datascrapeGui as Scrape
import components.webCrawler.webCrawlerGui as Crawler

class sideMenu(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        frame = Frame(master)
        frame.pack()
    
        self.sideMenuFrame = Frame(master, bg='#80c1ff')
        self.sideMenuFrame.place(relx=0.05, rely=0, relwidth=0.1, relheight=0.75, anchor='n')

        self.crawlerRouteButton = Button(self.sideMenuFrame, text="CRAWLER", command=lambda:controller.show_frame(Crawler.webCrawlerGui))
        self.crawlerRouteButton.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)

        self.dataScrapeRouteButton = Button(self.sideMenuFrame, text="DATASCRAPE", command=lambda:controller.show_frame(Scrape.datascrapeTable))
        self.dataScrapeRouteButton.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        