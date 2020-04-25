import sys
import csv

if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(1)

def FindNumb(txt,tf):
    start = 0
    maxi = 0
    while start < len(txt):
        cont = 0
        x = txt[start:len(txt)].find(tf)
        start = start + x + len(tf)
        cont += 1
        while txt[start:len(txt)].find(tf) == 0:
            cont += 1
            start += len(tf)
            if start > len(txt):
                break
        maxi = max(cont,maxi)
    return maxi


large = ["name", "AGATC", "TTTTTTCT" ,"AATG" ,"TCTAG" ,"GATA" , "TATC", "GAAA" ,"TCTG"]
small = ["name","AGATC","AATG","TATC"]

file1 = open(sys.argv[2],"r")
s = file1.read()

if sys.argv[1] == "databases/large.csv":
    x = []
    for i in range(9):
        x.append(FindNumb(s,large[i]))                 #Find the way to find longest repeating substring in python
    with open(sys.argv[1], mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)          #Stores the data of csv file in memory
        for row in csv_reader:
            c = 1
            for i in range(1,9):
                if x[i] != int(row[large[i]]):
                    c = 0
                    break
            if c == 1:
                print(row[large[0]])
                sys.exit(0)
                break
        print("No match")
        sys.exit(1)
else:
    x = []
    for i in range(4):
        x.append(FindNumb(s,small[i]))
    with open(sys.argv[1], mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            c = 1
            for i in range(1,4):
                if x[i] != int(row[small[i]]):
                    c = 0
                    break
            if c == 1:
                print(row[small[0]])
                sys.exit(0)
                break
        print("No match")
        sys.exit(1)






