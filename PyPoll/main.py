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
OutputFile = os.path.join(os.path.dirname(__file__), "analysis", "election_results.txt")

# Construct empty lists to bring in data, and dictionary for processing:
Headers=[]
IDs=[]
Candidate=[]
Votes={}
Names = []
Pct_of_Votes={}


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
           #Append column column 2 to Candidate 
            Candidate.append(row[2])
            line_count += 1



#Tally the votes: Look at candidate list, and count the number of times each candidate received a vote
for individual in Candidate:
  if individual not in Votes:  #This is the first occurence of a unique candidate name, add key to dict and set value = 1
    Votes[individual] = 1
  else:
    Votes[individual] += 1     #This is NOT the first occurrence of a unique candidate name, increment existing value by 1

#Calculations: 

Winner = max(Votes, key=Votes.get)

Total_Vote_Count = sum(Votes.values())


#Final output... 
#Construct list of f-strings for printing to file and screen (allows the variables to be reused in both output streams, instead of calculating over the input file twice)
Output_Text = [
                "Election Results",
                "-------------------------",
                f'Total Votes: {Total_Vote_Count}',
                "-------------------------"
              ]

for key, value in Votes.items():
  Output_Text.append(f'{key}: {value/Total_Vote_Count:.3%} ({value})')

Output_Text.append("-------------------------")
Output_Text.append(f'Winner: {Winner}')
Output_Text.append("-------------------------")

f = open(OutputFile, 'w') 
for each_line in Output_Text:
    # prints to output file
    f.write(each_line + '\n')
    # Prints to console
    print(each_line)

# Close the file
f.close()
#####End of Script#####