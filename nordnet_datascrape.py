import pandas as pd
import requests
from bs4 import BeautifulSoup
import googleDriveService as googleDrive
import os
import datetime

dataGlobal = [] 
data = []
keys = []
outputFileName = "nordnetStockData.csv"

def getNordnetData():
    global data
    global keys
    nordnet_response = requests.get("https://www.nordnet.se/mux/web/marknaden/kurslista/aktier.html?marknad=Sverige&lista=1_1&large=on&sektor=0&subtyp=price&sortera=&sorteringsordning=")
    nordnet_data = nordnet_response.content
    nordSoup = BeautifulSoup(nordnet_data, "html.parser")
    table = nordSoup.find("table")
    columns = nordSoup.find('table').findAll('thead')
    keys = [[th.findChildren(text=True) for th in tr.findAll("th")] for tr in columns]

    for row in table.tbody.findAll('tr'):
        dataRow = [
                row.findAll('td')[3].text.strip(),
                row.findAll('td')[5].text.strip(),
                row.findAll('td')[6].text.strip(),
                row.findAll('td')[7].text.strip(),
                row.findAll('td')[8].text.strip(),
                row.findAll('td')[9].text.strip(),
                row.findAll('td')[11].text.strip(),
                row.findAll('td')[12].text.strip(),
                row.findAll('td')[13].text.strip(),
                row.findAll('td')[14].text.strip()
        ]
    data.append(dataRow)

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

def cleanData(dirty_df, dirty_column, dirt):
    clean_df = dirty_df
    clean_df[dirty_column] = dirty_df[dirty_column].replace(dirt, "", regex=True)
    return clean_df

def numData(nonFloatDF, columnsToFloat):
    FloatDF = nonFloatDF
    for column in columnsToFloat:
        FloatDF.column = pd.to_numeric(FloatDF.column)
    return FloatDF

def updateFile(filename, dataToWrite):
    if os.path.isfile(filename):
         """ csv_df = pd.read_csv(filename)
        export_data = pd.concat([csv_df, dataToWrite])
        export_data.to_csv(filename) """
    else:
        dataToWrite.to_csv(filename, encoding = 'utf-8')  
    googleDrive.saveResultToGoogleDrive(filename)

getNordnetData()
filtered_keys = extractDataByTableElements(keys)[1:]
dataGlobal = []
#filtered_data = filterData()
Nordnet_df = pd.DataFrame(data, columns = filtered_keys)
updateFile(outputFileName, Nordnet_df)
""" Nordnet_df = cleanData(Nordnet_df, "%", "[\%]")
Nordnet_df = numData(Nordnet_df, filtered_keys[2:10])
Nordnet_df["Date"] = datetime.date()

 """