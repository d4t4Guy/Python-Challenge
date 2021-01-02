#PyBank main

# Requirements
# Input = budget_data.csv in resources folder
# Outputs (need to print both to terminal and txt file):
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

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

STEPS
Import csv lib
read in file columns to individual lists
loop through net income list (list comprehension?) and calculate delta as i+1 value - i value
Calculate summary statistics as listed in requirements and assign to output variables
Construct f-strings
Print to text file
Print to terminal
 """

import os
import csv


with open('./Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'row {line_count} reads {", ".join(row)}')
            line_count += 1
#    print(f'the first element reads: {row[0]}, and the second element reads: {row[1]}')
#   print(f'the second element reads: {row[1]}')
#   print(f'The length of the list is: {len(row)}')
    print(f'Processed {line_count} lines.') 

print("done!")