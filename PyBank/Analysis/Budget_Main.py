# Import necessary modules
import os
import csv

BankCSV = os.path.join('..','Python\Instructions\PyBank\Resources\budget_data.csv')

M = []                 #Turns the csv into individual lists per column
PL = []
#Date/Profit/Losse

with open(BankCSV, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  #splits the data
    header = next(csvreader)                        #CSVFile has a Header
    for row in csvreader:
        M.append(row[0])
        PL.append(int(row[1]))

PLdiff = []
for a, b in zip(PL[0::], PL[1::]):      #Creates a new list for in >change< in PL
    PLdiff.append(int(b)-int(a))        #called PLdiff, using zip

PLdiffAvg = sum(PLdiff) / len(PLdiff)   #Takes the average in PLdiff

PLH = max(PLdiff)
for _ in PLdiff:                #Circles through Dif
    if(PLH == _):               #If Min = Current Val..
        PLMi = PLdiff.index(_)  #Set Variable to Current Val's index

PLL = min(PLdiff)
for _ in PLdiff:                #Circles through Dif
    if(PLL == _):               #If Min = Current Val..
        PLLi = PLdiff.index(_)  #Set Variable to Current Val's index

Line1 = "\nFinancial Analysis" + '\n' + "-------------------------" + '\n' + "Total Months: {}\n".format(len(M))
Line2 = "Total P/L: ${}\n".format(sum(PL))
Line3 = "Average Change: ${}\n".format(round(float(PLdiffAvg), 2))
Line4 = "Greatest Increase in Profits: {} (${})\n".format(M[PLMi+1], PLH)
Line5 = "Greatest Decrease in Profits: {} (${}) \n".format(M[PLLi+1], PLL)

print(Line1 + Line2 + Line3 + Line4 + Line5)

with open('Output.txt', 'w') as OutputFile:                  #writes to a text file
    OutputFile.write(Line1 + Line2 + Line3 + Line4 + Line5)
