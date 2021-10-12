import csv

s = open("prx.txt","a")
with open('socks4.csv', 'r') as f:
    for row in csv.reader(f):
        print(row[0])
        s.write("%s\n"%row[0])