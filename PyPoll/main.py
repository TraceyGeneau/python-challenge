#this is the main .py for PyBank

#First import OS to allow us to work accross operating systems

import os

#import module for reading csv files
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
#another way to calculate this is to use a loop with row not blank until it hits a blank one and count each of those rows
    
    #C SV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    count=len(list(csvreader))
    print("Election Results")
    print("---------------------------------------")
    print("The number of votes are " +str(count))
    

#make a list that only contains one of each candidate name
votes = 0
seen_candidates = []
candidate_votes = {}
Percent_Votes = []
Final_Votes = []
Final_Votes_dict = {}
Vote_List = []

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        #print(row[2])
        candidate_name = row[2]

        #What we are doing is looking through the list and if we see a new cadidate it is added to the seen_candidates.  The elseif says that 
        #we will add one tot he cadidate votes for each of the same candidate until we get to one that is NOT IN the group.  this will continue until we have 
        #all the votes and cadidates accounted for.

        if candidate_name not in seen_candidates:
            seen_candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#pull the total votes out of the dictionary *Reference to tutorialspoint.com 

votes_list = list(candidate_votes.values())

for i in votes_list:
    percent = round((i/count*100),2)
    Percent_Votes.append(str(percent)+"%")


#turned three lists into one list then made a dictionary out of it
# Reference for enumerating a list come from atus.com
Final_Votes=list(zip(seen_candidates,Percent_Votes,votes_list))
for index,element in enumerate(Final_Votes):
    Final_Votes_dict[index] = element

popular = max(Final_Votes, key=lambda tup:tup[1])

#[x][y] gives rows and columns in the list Final_Votes
print("---------------------------------------")
print(f'{Final_Votes[0][0]}  {Final_Votes[0][1]}  ({Final_Votes[0][2]})')
print(f'{Final_Votes[1][0]}  {Final_Votes[1][1]}  ({Final_Votes[1][2]})')
print(f'{Final_Votes[2][0]}  {Final_Votes[2][1]}  ({Final_Votes[2][2]})')
print("---------------------------------------")


print("Winner: " +str(popular[0]))

output_path = os.path.join('Analysis', 'analysis.txt')
with open(output_path, 'w') as analysis_file:
    analysis_file.write("Election Results")
    analysis_file.write("\n")
    analysis_file.write("---------------------------------------")
    analysis_file.write("\n")
    analysis_file.write("The number of votes are " +str(count))
    analysis_file.write("\n")
    analysis_file.write("---------------------------------------")
    analysis_file.write("\n")
    analysis_file.write(f'{Final_Votes[0][0]}  {Final_Votes[0][1]}  ({Final_Votes[0][2]})')
    analysis_file.write("\n")
    analysis_file.write(f'{Final_Votes[1][0]}  {Final_Votes[1][1]}  ({Final_Votes[1][2]})')
    analysis_file.write("\n")
    analysis_file.write(f'{Final_Votes[2][0]}  {Final_Votes[2][1]}  ({Final_Votes[2][2]})')
    analysis_file.write("\n")
    analysis_file.write("---------------------------------------")
    analysis_file.write("\n")


print("Winner: " +str(popular[0]))

#References
#"How to Convert and Dictionary to a list" https://www.tutorialspoint.com/How-to-convert-Python-Dictionary-to-a-list#:~:text=To%20obtain%20a%20list%20of,using%20the%20list()%20function.
#"Python-Converting lsts to dictionsaries" https://www.atatus.com/blog/python-converting-lsts-to-dictionaries/

    







        


   
        




  
            

    
        
       


