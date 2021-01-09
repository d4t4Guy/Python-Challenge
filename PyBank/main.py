#PyBank main

# Requirements
# Input = budget_data.csv in resources folder
# Outputs (need to  both to terminal and txt file):
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

#Assumptions:
# A1 This file, main.py is in a directory with a budget_data.csv file in ./resources directory
# A2 Budget_data file is a csv with months in the first column, and Profit/Loss in the second column
# A3 This directory also has a sub-directory named ./analysis 


#import modules needed to read csv and write to file
import os
import csv

#Define input and output filenames for later use
InputFile = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")
OutputFile = os.path.join(os.path.dirname(__file__), "Analysis", "PnL_Summary.txt")


#create empty lists to append to them via loop
Headers = []
PnLMonth = []
PnLNOI = []
Month_Delta=[]

#read in data row-by-row. 
with open(InputFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        #store headers in their own list
        if line_count == 0:
            Headers.append(row[0])
            Headers.append(row[1])
            line_count += 1
        else:
           #Append Month to PnLMonth[] and Profit/Loss to PnLNOI (NOI => net operating income)  
            PnLMonth.append(row[0])
            PnLNOI.append(int(row[1]))
            line_count += 1



Month_Delta.append(0)  #populate a zero to the first month's (Month_Delta[0]) change column. NaN would probably be more appropriate but that generates a type clash when using summary functions.

for i in range(1,len(PnLNOI)):
    Month_Delta.append((PnLNOI[i]) - (PnLNOI[i-1]))
    
###Summary stats
Total_month_cnt = len(PnLMonth)
Total_NOI = sum(PnLNOI)
Delta_Count = len(PnLNOI)-1
Total_Delta = sum(Month_Delta)
Average_Delta = Total_Delta/(Delta_Count)
Max_Delta = max(Month_Delta)
Min_Delta = min(Month_Delta)

#return indices of most improved and most deteriorated months
Max_Index = Month_Delta.index(Max_Delta) 
Min_Index = Month_Delta.index(Min_Delta) 

#return month values associated with greatest and least deltas
Max_Delta_Month = PnLMonth[Max_Index]
Min_Delta_Month = PnLMonth[Min_Index]


#Final output... 
#Construct list of f-strings for printing to file and screen (allows the variables to be reused in both output streams, instead of calculating over the input file twice)
Output_Text = [
                "Financial Analysis",
                "----------------------------",

                f'Total Months:  {Total_month_cnt}',
                f'Total:  {Total_NOI}',
                f'Average Change:  {round(Average_Delta,2)}',
                f'Greatest Increase In Profits: {Max_Delta_Month} ({Max_Delta})',
                f'Greatest Decrease in Profits:  {Min_Delta_Month} ({Min_Delta})',
              ]

f = open(OutputFile, 'w') 
for each_line in Output_Text:
    # prints to output file
    f.write(each_line + '\n')
    # Prints to console
    print(each_line)

# Close the file
f.close()

##### End of script #####
