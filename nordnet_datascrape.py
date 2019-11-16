import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import googleDriveService as googleDrive

dataGlobal = [] 
data = []
keys = []

def getNordnetData():
    global data
    global keys
    nordnet_response = requests.get("https://www.nordnet.se/mux/web/marknaden/kurslista/aktier.html?marknad=Sverige&lista=1_1&large=on&sektor=0&subtyp=price&sortera=&sorteringsordning=")
    nordnet_data = nordnet_response.content
    nordSoup = BeautifulSoup(nordnet_data, "html.parser")
    table = nordSoup.find("table", id = "kurstabell")
    rows = table.findAll('tr')
    columns = table.findAll('thead')
    data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
    keys = [[th.findChildren(text=True) for th in tr.findAll("th")] for tr in columns]

def extractDataByTableElements(listOfTableElements):
    for element in listOfTableElements: 
        if isinstance(element, list):
            extractDataByTableElements(element)
        else:
            dataGlobal.append(element) 
    return dataGlobal 

def filterData():
    filtered_data_list = []
    filtered_data = list(filter(lambda a: a != " ", (filter(lambda a: a != "\n", extractDataByTableElements(data)))))
    while filtered_data:
        filtered_data_list.append(filtered_data[0:11])
        del filtered_data[0:11]
    return filtered_data_list

getNordnetData()
filtered_data = filterData()
dataGlobal = []
filtered_keys = extractDataByTableElements(keys)

Nordnet_df = pd.DataFrame(filtered_data, columns = filtered_keys)
googleDrive.saveResultToGoogleDrive(Nordnet_df, 'nordnetStockData.txt')
googleDrive.downloadFromGoogleDrive('nordnetStockData.txt')