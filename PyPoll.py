
#    Total number of votes cast
#     A complete list of candidates who received votes
#     Total number of votes each candidate received
#     Percentage of votes each candidate won
#     The winner of the election based on popular vote

# Dependencies 
import csv
import os

# Assign variable and load file from path
file_to_load = os.path.join('.', 'Resources', 'election_results.csv')
# Assign variable and create and save file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open csv and read file then assign variable 
with open(file_to_load, "r") as election_data: 
     file_reader=csv.reader(election_data)

     header=next(file_reader)
     print(header)
     #print(election_data)





with open(file_to_save, "w") as txt_file:
     txt_file.write("Arapahoe.=\nDenver\nJefferson") 
