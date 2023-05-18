#this is the main .py for PyBank

#First import OS to allow us to work accross operating systems

import os

#import module for reading csv files
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')

#creating a place to put the data from profit loses *Reference to Kelly Moira How to read csv files


with open(csvpath) as csvfile:

    
 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 

    csv_header = next(csvreader)
    count=len(list(csvreader))
    print("Final Analysis")
    print("----------------------------------------")
    print("The number of months are " +str(count))
    
    

profitloss = [] #list for storage of my numbers
profitchange = []
date = []

with open(csvpath) as csvfile:
    
 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first *Reference from Programs and Me youtube
    csv_header = next(csvreader)
    for row in csvreader:
        profitloss.append(int(row[1])) #adds numbers to list

        sumprofitloss = 0 #this is the variable that is going to store out sum
        for i in profitloss:
            sumprofitloss = sumprofitloss+i
    print("Total: $"+ str(sumprofitloss))
    
    avgchange = ((profitloss[count-1])-(profitloss[0]))/(count-1) #by putting in the numbers in the square brakets it picks the row number
    print("Average Change: $" + str(round(avgchange,2))) #round will put decimals (,2) to two places

num_rows = 0
change = []

with open(csvpath) as csvfile:
    
 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first  *Reference to Bobbyhazd.com for min max
    # Referenced Stacked Overflow to determine the change from one month to the next
    csv_header = next(csvreader)
    for row in csvreader:
        date.append(row[0])
    
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)
        previous_revenue = 0

        for row in csvreader:
            revenue = int(row[1])
            num_rows += 1
            change.append([row[0], revenue - previous_revenue])
            previous_revenue = revenue

    increase = max(change, key=lambda tup:tup[1])
    decrease = min(change, key=lambda tup:tup[1])

    print(f'Greatest Increase In Profits: {increase[0]}  (${str(increase[1])})')
    print(f'Greatest Increase In Profits: {decrease[0]}  (${str(decrease[1])})')
    

output_path = os.path.join('Analysis', 'analysis.txt')
with open(output_path, 'w') as analysis_file:
    analysis_file.write("Final Analysis")
    analysis_file.write("\n")
    analysis_file.write("----------------------------------------")
    analysis_file.write("\n")
    analysis_file.write("The number of months are " + str(count)) 
    analysis_file.write("\n")                                                             
    analysis_file.write("Total: $"+ str(sumprofitloss))
    analysis_file.write("\n")
    analysis_file.write("Average Change: $" + str(round(avgchange,2)))
    analysis_file.write("\n")
    analysis_file.write(f'Greatest Increase In Profits: {increase[0]}  (${str(increase[1])})')
    analysis_file.write("\n")
    analysis_file.write(f'Greatest Increase In Profits: {decrease[0]}  (${str(decrease[1])})')    
    analysis_file.write("\n")


#References
#How to print a csv file https: //earthly.dev/blog/csv-python
#Adding an appended list https://www.youtube.com/watch?v=B-JzsJvdhGg&ab_channel=ProgramsAndMe
#min max of a value in a list https://bobbyhadz.com/blog/python-find-min-max-value-in-list-of-tuples#find-min-and-max-values-in-a-list-of-tuples-in-python
#Determining Change Value in a Row https://stackoverflow.com/questions/53474110/python-determine-change-in-value-from-one-period-to-the-next
#How to put a column from a CVS file into a dictioary https://www.youtube.com/watch?v=DRqEk1ipv5E&ab_channel=DataEngUncomplicated