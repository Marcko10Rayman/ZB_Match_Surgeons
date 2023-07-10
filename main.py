import os
import glob
import csv
from tkinter.filedialog import askopenfilename
import pandas as pd

#*Variables
project_path = os.getcwd()
FOLDER_CSV = os.path.join(project_path,'data')
list_csv = []
new_csv = []


def csv_converter(title, data):
    if not os.path.exists(FOLDER_CSV):
        os.mkdir(FOLDER_CSV)
    path_csv = os.path.join(FOLDER_CSV, title)
    data_frame = pd.DataFrame(data)
    data_frame.to_csv(path_csv, encoding='utf-8', index=False)
    print('\n------> Your csv can found it in the following path : ' + str(path_csv))
    
def read_csv(path):
    with open(path, encoding='utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)
        if csvReader :
            for row in csvReader :
                list_csv.append(row);
        else:
            print(':::::: The CSV is empty :::::');
    return list_csv

def analisys_csv(accounts, contentversions):
    for _, contentversion in enumerate(contentversions):
        for _, account in enumerate(accounts):
            if contentversion.get('TITLE') == account.get('NPI__c') and contentversion.get('TITLE') and account.get('NPI__c') :
                #print('content = ' + str(contentversion.get('TITLE'))+ ' == account = ' + str(account.get('NPI__c')))
                print('Proccessing ......');
                row = {
                    'Id' : account.get('Id'),
                    'NPI__c' : account.get('NPI__c'),
                    'btydev__Picture_Id__pc' : contentversion.get('ID')
                }
                new_csv.append(row)
    return new_csv

def main() :
    print('------- Start Script -------\n')
    print('Functionality : ')
    print('This script is created to related the accounts with the contentversion ids by NPI number of the doctor.\n')
    PathFileAccounts = askopenfilename(title='Select the Account csv to load',
                        filetypes = (("CSV Files","*.csv"),))
    print('>>>>>>>> The path of the account csv is : ' + str(PathFileAccounts))
    PathFileContentVersion = askopenfilename(title='Select the Content Version csv to load',
                        filetypes = (("CSV Files","*.csv"),))
    print('>>>>>>>> The path of the content version csv is : ' + str(PathFileContentVersion) +'\n')
    
    if not PathFileAccounts:
        print('::::: WARNING : You have to choose a csv with accounts data :::::::')
    elif not PathFileContentVersion:
        print('::::: WARNING : You have to choose a csv with content-version data :::::::')
    else :
        print('::::::: Processing data :::::::')
        print('Please, wait a moment')
        AccountData = read_csv(PathFileAccounts)
        ContentData = read_csv(PathFileContentVersion)
        data_csv = analisys_csv(AccountData,ContentData)
        csv_converter('Accounts.csv', data_csv)
        print('\n------- Finish Script -------')

main()