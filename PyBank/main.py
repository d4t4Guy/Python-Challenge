#PyBank main

# Requirements
# Input = budget_data.csv in resources folder
# Outputs (need to print both to terminal and txt file):
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

#Assumptions:
# This file, main.py is in a directory with a budget_data.csv file in ./resources directory
# Budget_data file is a csv with months in the first column, and Profit/Loss in the second column
#  

#psuedo-code:
""" Variables: 
OUTPUTS
total_month_cnt as integer 
Net_total (over P&L column) as float
Avg_Delta as float 
Max_Delta as float
Min_Delta as float 
Best_Month, Worst_Month as date

INPUTS
Months[]
Net_Income[]

PROCESS
Month_Delta[]
Headers[]
PnLMonth[]
PnLNOI[]


STEPS
Import csv lib
create empty list for storage of headers
read in file columns to individual lists
loop through net income list and calculate delta as  NOI in that month, less that of the prior month
Calculate summary statistics as listed in requirements and assign to output variables
Construct f-strings
print to text file
print to terminal
 """

#import modules needed to read csv and write to file
import os
import csv

dirname = os.path.dirname(__file__)  
print('dirname: ', dirname)
relativePath = "resources/budget_data.csv"

print(dirname + relativePath)

fullpath = os.path.join(os.path.dirname(__file__), relativePath)

print("Full Path: ", fullpath)



Headers = []
PnLMonth = []
PnLNOI = []
Month_Delta=[]

#read in data row-by-row. Append Month to PnLMonth[] and Profit/Loss to PnLNOI (NOI => net operating income) 
with open(os.path.join(os.path.dirname(__file__),'Resources/budget_data.csv')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            Headers.append(row[0])
            Headers.append(row[1])
            line_count += 1
        else:
            PnLMonth.append(row[0])
            PnLNOI.append(int(row[1]))
            line_count += 1


Delta_Count = len(PnLNOI)
Month_Delta.append(0)  #populate a zero to the first month's (Month_Delta[0]) change column

for i in range(1,Delta_Count):
    Month_Delta.append((PnLNOI[i]) - (PnLNOI[i-1]))
    
###Summary stats
Total_month_cnt = len(PnLMonth)
Total_NOI = sum(PnLNOI)
Total_Delta = sum(Month_Delta)
Average_Delta = Total_Delta/(Delta_Count-1) #subtracting one to account for zero delta in month 0
Max_Delta = max(Month_Delta)
Min_Delta = min(Month_Delta)

#return indices of most improved and most deteriorated months
Max_Index = Month_Delta.index(Max_Delta)
Min_Index = Month_Delta.index(Min_Delta)

#return month values associated with greatest and least deltas
Max_Delta_Month = PnLMonth[Max_Index]
Min_Delta_Month = PnLMonth[Min_Index]


#Final output. Redirect stdout to file "PyBank.txt" and then cat PyBank.txt to terminal
print("Financial Analysis")
print("----------------------------")

print(f'Total Months:  {Total_month_cnt}')
print(f'Total:  {Total_NOI}')
print(f'Average Change:  {round(Average_Delta,2)}')

print(f'Greatest Increase In Profits: {Max_Delta_Month} ({Max_Delta})')
print(f'Greatest Decrease in Profits:  {Min_Delta_Month} ({Min_Delta})')

