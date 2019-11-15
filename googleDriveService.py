import pandas as pd
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

def saveResultToGoogleDrive(dataToUpload, filename):
    deleteFileIfPresent(filename)
    dataFile = drive.CreateFile({'title': filename + '.txt'})
    dataToUpload.to_csv('output.csv', encoding = 'utf-8')
    dataFile.SetContentFile('output.csv')
    dataFile.Upload()

def deleteFileIfPresent(filename):
    file_list = drive.ListFile().GetList()
    for file1 in file_list:
        if file1['title'] == filename + '.txt':
            file1 = drive.CreateFile({'id': file1['id']})
            file1.Delete()