import pandas as pd
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

def saveResultToGoogleDrive(filename):
    deleteFileIfPresent(filename)
    dataFile = drive.CreateFile({'title': filename})
    dataFile.SetContentFile(filename)
    dataFile.Upload()

def checkFileIfPresent(filename):
    file_list = drive.ListFile().GetList()
    for file1 in file_list:
        if file1["title"] == filename:
            return file1['id']
        else:
            continue
    return None


def deleteFileIfPresent(filename):
    file_id = checkFileIfPresent(filename)
    if file_id:
        file1 = drive.CreateFile({'id': file_id})
        file1.Delete()

def downloadFromGoogleDrive(filename):
    file_id = checkFileIfPresent(filename)
    if file_id:
        file1 = drive.CreateFile({'id': file_id})
        file1.GetContentFile(file1["title"])



