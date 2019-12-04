import pandas as pd
import requests
from bs4 import BeautifulSoup
import googleDriveService as googleDrive
import os
from datetime import date
from more_itertools import unique_everseen

dataGlobal = [] 
data = []
namn = []
keys = []
outputFileName = "nordnetStockData.csv"

def getNordnetData():
    global data
    global keys
    global namn
    data = []
    keys = []
    namn = []
    nordnet_response = requests.get("https://www.nordnet.se/marknaden/aktiekurser?exchangeCountry=SE&exchangeList=se%3Aomxs30")
    nordnet_data = nordnet_response.content
    nordSoup = BeautifulSoup(nordnet_data, "html5lib") #"html.parser"
    table = nordSoup.find("table")
    columns = nordSoup.find('table').findAll('thead')
    keys = [[th.findChildren(text=True) for th in tr.findAll("th")] for tr in columns]
    data = [item.get_text(strip=True) for item in nordSoup.select("span.c02474")]
    namn = [item.get_text(strip=True) for item in table.select("a.c02447")] #strip("'b")
    namn = list(unique_everseen(namn))

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
        temp_list = []
        temp_list.extend(filtered_data[:5])
        temp_list.extend(filtered_data[7:10])
        filtered_data_list.append(temp_list)
        del filtered_data[:10]
    return filtered_data_list

def cleanData(dirty_df, dirt, dirty_column=False, replace_value = False, replace=False):
    clean_df = dirty_df
    if replace == False:
        if dirty_column == False:
            clean_df = clean_df.replace(to_replace=dirt, value="", regex=True)
        else:
            clean_df[dirty_column] = clean_df[dirty_column].replace(to_replace=dirt, value="", regex=True)
    elif replace == True and replace_value == False:
        print("Need replace value")
    else:
        if dirty_column == False:
            clean_df = clean_df.replace(to_replace=dirt, value=replace_value, regex=True)
        else:
            clean_df[dirty_column] = clean_df[dirty_column].replace(to_replace=dirt, value=replace_value, regex=True)
    return clean_df

def numData(nonFloatDF, columnsToFloat):
    FloatDF = nonFloatDF
    for column in columnsToFloat:
        FloatDF[column] = pd.to_numeric(FloatDF[column])
    return FloatDF

def updateFile(filename, dataToWrite):
    if os.path.isfile(filename):
         """ csv_df = pd.read_csv(filename)
        export_data = pd.concat([csv_df, dataToWrite])
        export_data.to_csv(filename) """
    else:
        dataToWrite.to_csv(filename, encoding = 'utf-8')  
    #googleDrive.saveResultToGoogleDrive(filename)


def runDatascrape():
    global dataGlobal
    getNordnetData()
    filtered_keys = extractDataByTableElements(keys)[1:]
    dataGlobal = []
    filtered_data = filterData()
    Nordnet_df = pd.DataFrame(filtered_data, columns = filtered_keys[1:9])
    Nordnet_df[filtered_keys[0]] = namn
    today = date.today()
    today_text = int(today.strftime("%y%m%d"))
    Nordnet_df["Date"] = today_text
    Nordnet_df = cleanData(Nordnet_df, "%", 'Idag %')
    Nordnet_df = cleanData(Nordnet_df, "MSEK", replace=True, replace_value="000000")
    Nordnet_df = cleanData(Nordnet_df, "SEK")
    Nordnet_df = cleanData(Nordnet_df, "\+")
    Nordnet_df = numData(Nordnet_df, filtered_keys[1:9])
    print(Nordnet_df)
    updateFile(outputFileName, Nordnet_df)
    return Nordnet_df

runDatascrape()