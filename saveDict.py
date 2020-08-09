import csv
import os

def saveDict(dictObj, path):
   w = csv.writer(open("{}.output.csv", "w").format(path))
   for key, val in dictObj.items():
       w.writerow([key, val]) 



#def loadDict(path)

def main():
    dict1 = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
    path = input("Please enter the path you would like to save to: ")
    saveDict(dict1, path)

if __name__ == '__main__':
    main()
