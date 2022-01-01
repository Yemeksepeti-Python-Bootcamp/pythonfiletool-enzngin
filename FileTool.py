import pandas as pd
import numpy as np

class crudCSV:


    def __init__(self,path,fields = None):
        if fields is not None: #Yeni bir CSV oluşturacaksak kullanılacak constructor
            self.path = path
            self.fields = fields
            self.createCSV(fields)
        if fields is None: #Varolan CSV üzerinden işlem yapılacaksa kullanılacak constructor
            self.path = path
            self.getCSV()

    def createCSV(self,fields):
        df = pd.DataFrame(columns=fields)
        df.to_csv(self.path, sep=";", encoding='utf-8', columns=fields, header=fields, index=False)
        print(self.path, " dizinine csv oluşturuldu")

    def getCSV(self):
        df = pd.read_csv(self.path,sep = ";")
        print(df)
        return df

    def addData(self,list): #Column sayısı kadar ve aynı sırayla veri tutan bir lsite(tek rowa karşılık gelecek)
        df = self.getCSV()
        addRow = pd.Series(list, index=df.columns)
        df = df.append(addRow,ignore_index = True)
        df.to_csv(self.path, sep=";", encoding='utf-8', index=False)
        print(df)

    def deleteData(self,index):
        df = self.getCSV()
        df = df.drop(index)
        df.to_csv(self.path, sep=";", encoding='utf-8', index=False)
























