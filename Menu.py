import FileTool as ft

class TerminalMenu:

    def showMainMenu(self):
        print("-Press 1 for create a new CSV file \n-Press 2 for work on an already exist CSV file")
        x = input()
        if(x == "1"):
            print("Enter the path and fields.")
            print("Path: ", end = "")
            path = input()
            print("Fields(Arada boşluk bırakarak giriniz!): ", end = "")
            fields = input()
            ftObj = ft.crudCSV(path,fields.split())
            self.operationsMenu(ftObj)
        if (x == "2"):
            print("Enter the path of the existing CSV file")
            print("Path: ", end=" ")
            path = input()
            ftObj = ft.crudCSV(path)
            self.operationsMenu(ftObj)

    def operationsMenu(self,csvObj):
        print("Operation list")
        print("-Press 1 for read the CSV file \n-Press 2 for add row to the CSV file \n-Press 3 for delete row from the CSV file")
        print("-Press 4 for update row on the CSV file \n-Press 5  for search on the CSV file  \n-Press 6 for copy all data to another CSV file")
        print("-Press 4 for search on the CSV file \n-Press 5 for update row on the CSV file \n-Press 6 for copy all data to another CSV file")
        x = input()
        if(x == "1"):
            print(csvObj.getCSV())
        elif(x == "2"):
            self.insertMenu(csvObj)
        elif(x == "3"):
            self.deleteMenu(csvObj)
        elif(x == "4"):
            self.updateMenu(csvObj)


    def insertMenu(self, csvObj):
        print("Enter the data you want to add in the column order, with spaces in between.")
        print("Columns: ", csvObj.getColumns())
        print("Data for add: ", end = "")
        x = input()
        csvObj.addData(x.split())

    def deleteMenu(self, csvObj):
        print(csvObj.getCSV())
        print("Enter the index number of the record you want to delete.")
        print("Index number :", end = "")
        x = input()
        csvObj.deleteData(int(x))

    def updateMenu(self, csvObj):
        print(csvObj.getCSV())
        print("Enter the index, column, new data of the record you want to update.")
        print("Index number: ", end = "")
        index = input()
        print("Column : ", end="")
        column = input()
        print("New data: ", end="")
        data = input()
        csvObj.updateByIndex(int(index),column,data)












