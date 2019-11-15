import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

nordnet_response = requests.get("https://www.nordnet.se/mux/web/marknaden/kurslista/aktier.html?marknad=Sverige&lista=1_1&large=on&sektor=0&subtyp=price&sortera=&sorteringsordning=")
nordnet_data = nordnet_response.content
nordSoup = BeautifulSoup(nordnet_data, "html.parser")
table = nordSoup.find("table", id = "kurstabell")
rows = table.findAll('tr')
data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows] 
columns = table.findAll('thead')
keys = [[th.findChildren(text=True) for th in tr.findAll("th")] for tr in columns]

def extract_list(list_input):
    extracted_data=[]
    for item1 in list_input: 
        if isinstance(item1, list):
            for item2 in item1:
                if isinstance(item2, list):
                    for item3 in item2:
                        extracted_data.append(item3)
                else:
                    extracted_data.append(item2)
        else:
            extracted_data.append(item1)
    return extracted_data

extracted_data = extract_list(data)
filtered_keys = extract_list(keys)

filtered_data = list(filter(lambda a: a != "\n", extracted_data))
filtered_data2 = list(filter(lambda a: a != " ", filtered_data))

filtered_data2_list = []
while filtered_data2:
    filtered_data2_list.append(filtered_data2[0:11])
    del filtered_data2[0:11]
Nordnet_df = pd.DataFrame(filtered_data2_list, columns = filtered_keys)
print(Nordnet_df)