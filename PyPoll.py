#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on poplular vote

#Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file.
with open(file_to_load) as election_data:
    
    #To do: perform analysis.
    print(election_data)

#Add our dependencies.
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader= csv.reader(election_data)

    #Read and Print the header row.
    headers = next(file_reader)
    print(headers)
