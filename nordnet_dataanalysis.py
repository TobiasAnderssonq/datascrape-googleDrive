import pandas as pd
import googleDriveService as googleDrive
from matplotlib import pyplot as plt
import os

def getData(filename):
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    elif googleDrive.checkFileIfPresent:
        googleDrive.downloadFromGoogleDrive(filename)
        df = pd.read_csv(filename)
    else:
        print("File not found")
    return df

def line_chart(df, column_x, column_y, sortbyColumn=None, sortbyValue=None):
    if sortbyColumn == None:
        plt.plot(df.column_x, df.column_y)
    else:
        sorted_df = df[df.sortbyColumn == sortbyValue]
        plt.plot(sorted_df.column_x, sorted_df.column_y)
    plt.show()

def hist_chart(df, column_x, column_y, sortbyColumn=None, sortbyValue=None):
    if sortbyColumn == None:
        plt.hist(df.column_x, df.column_y)
    else:
        sorted_df = df[df.sortbyColumn == sortbyValue]
        plt.hist(sorted_df.column_x, sorted_df.column_y)
    plt.show()

nordnet_df = getData("nordnetStockData.csv")
line_chart(nordnet_df, "Omsatt", "Date", "Aktie", "EQT AB")