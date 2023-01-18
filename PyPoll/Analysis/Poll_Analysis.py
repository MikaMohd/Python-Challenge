# Import necessary modules
import os
import csv

BankCSV = os.path.join('..','Python\Instructions\PyPoll\Resources\election_data.csv')

Bid = []                                #Turns the csv into individual lists per column
Count = []
Candid = []
#Ballot ID,County,Candidate             #This helps get an idea of what the CSV looks like

with open(BankCSV, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  #splits the data
    header = next(csvreader)                        #CSVFile has a Header
    for row in csvreader:                           #creates/loads all the lists.
        Bid.append(row[0])
        Count.append(row[1])
        Candid.append(row[2])



TotalVotes = (len(Bid))

line3 = ("\nElection Results\n------------------\nTotal Votes: {}\n------------------".format(TotalVotes))  #Stores print lines as a variable to write to the output file.
print(line3)                                                                                                           

UnqCand = []            #Makes a list for all the unique candidates
for _ in Candid:
    if _ not in UnqCand:
        UnqCand.append(_)

def CandidateVoteCounter(CandidateInp:str):         #Using functions for repetitive tasks
    UnqV = 0                                        #Inputs the Candidate (In this case from the UnqCand list)
    for _ in Candid:
        if _ == CandidateInp:                       #Adds 1 for each find of the input
            UnqV = UnqV + 1
    return UnqV                                     #returns the total count of the input.

def PercentConv(VoteInp:int):
    VotePercent = round((VoteInp/TotalVotes) * 100, 3)      #Makes a formatted percent out of input/total
    return VotePercent                                      #returns the formatted variable. 

CVotes = []
Percents = []
for _ in range(len(UnqCand)):        #Runs through the functions above to output each candidate's information and attach to lists
    CVotes.append(CandidateVoteCounter(UnqCand[int(_)]))    #makes a new list for Vote Totals per Unique Cand.
    Percents.append(PercentConv(CandidateVoteCounter(UnqCand[int(_)])))     #makes a new list for Percentage per Unique Cand.

    print("{}: {}% ({})".format(UnqCand[int("{}".format(_))], Percents[_], CVotes[_]))         #Prints Candidate, Respective Percentage and Total
    globals()["line{}".format(str(_))] = ("{}: {}% ({}) ".format(UnqCand[int("{}".format(_))], Percents[_], CVotes[_]))    # Saves the print line to add to the file.

WinnerP = max(Percents)              #Finds Max for the Percents
WinnerC = ""                         
for _ in Percents:                   #Runs through Percents.
    if(WinnerP == _):                #if max is found, set WinnerC to the index of the max.
        WinnerC = UnqCand[Percents.index(_)]       #navigates through the lists to find the winner based on percents.

line4 = ("---------------------\nWinner: " + str(WinnerC) + "\n---------------------\n")           #prints the last part of the analysis
print(line4)

with open('Output.txt', 'w') as OutputFile:                                                        #writes to a text file
    OutputFile.write(line3 + "\n" + line0 + "\n" + line1 + "\n" + line2 +  "\n" + line4)