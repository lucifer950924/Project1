import os , csv

class CSVReader:
    def __init__(self,testName):
        self.datDir = os.path.join(os.getcwd(),'TestData',f'{testName}.csv')
    
    def read_csv(self):
        try:
            with open(self.datDir, 'r' ) as file:
                reader = csv.reader(file)
                data = {}
                for row in reader:
                    data[row[0]] = row[-1]

            return data
        except FileNotFoundError:
            print(' Place the csv file with TestName.csv in the TestData folder')

 