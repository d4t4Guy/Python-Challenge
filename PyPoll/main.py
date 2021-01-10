# pyPoll - counts votes and returns summary
# input: CSV file containing voter id, county, candidate 

#output
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

#Example to print to console and to output file
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

#import modules needed to read csv and write to file
import os
import csv

#Define input and output filenames for later use
InputFile = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
OutputFile = os.path.join(os.path.dirname(__file__), "Analysis", "election_results.txt")


# steps
# Construct empty lists to bring in data, and dictionary for processing:
Headers=[]
IDs=[]
Candidate=[]
Votes={}

# Import id's into list; import votes into another list
  #read in data row-by-row. 
with open(InputFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        #store headers in their own list
        if line_count == 0:
            Headers.append(row[0])
            Headers.append(row[1])
            Headers.append(row[2])
            line_count += 1
        else:
           #Append column 0 to IDs and column 2 to Candidate 
            IDs.append(row[0])
            Candidate.append(row[2])
            line_count += 1

# #Show the top ten lines in each list ####For testing, remove before submit
# for i in range(0,9):
#   print(f'ID: {IDs[i]} -- candidate: {Candidate[i]}')
#   # Combine into dict with ID as key and candidate as value
# print(f'Count: {len(Candidate)}')
        # total nr votes cast = len(IDs)
        # Complete list of candidates who received votes: ??? - need to find out how to list distinct values in dict
        # Pct of votes per candidate
        # Total votes per candidate
        # Winner = Max(total votes)--> Candidate