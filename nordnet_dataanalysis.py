import pandas as pd
import googleDriveService as googleDrive
from matplotlib import pyplot as plt
import os

def getData(filename): #fortsätt här
    if os.path.isfile(filename):

def line_chart(df, column_x, column_y, sortbyColumn=None, sortbyValue=None):
    if sortbyColumn == None:
        plt.plot(df.column_x, df.column_y)
    else:
        sorted_df = df[df.sortbyColumn == sortbyValue]
        plt.plot(sorted_df.column_x, df.column_y)
    plt.show()

line_chart() #för att kunna lägga in df till denna