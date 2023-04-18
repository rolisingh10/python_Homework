#importing csv
import csv
import os

# Defining the set and dictionary

total_votes = 0
candidate_names = []
candidate_votes = {}
max_votes = 0
winner = ""
# find the path of the file to read
csvpath = r'C:\Users\rolis\OneDrive\Desktop\python_Homework\PyPoll\Resources\election_data.csv'
#opening the csv file to read
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skipping the header
    header = next(csvreader)
    #looping through each row in the file
    for row in csvreader:
        total_votes += 1
#print(total_votes)
        candidate_name = row[2]
        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            #print(candidate_names)
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1
#print(candidate_votes)
for candidate in candidate_votes:
   votes = candidate_votes.get(candidate) 
   #print(votes)
   
   
   if votes > max_votes:
       max_votes = candidate_votes[candidate]
       winner = candidate
#print(max_votes)
#print(winner)

print("Election Results")

print("----------------------")

print(f"Total Votes: {total_votes}")

print("-----------------------")

for candidate, votes in candidate_votes.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")


print("-----------------------")

print(f"Winner:{winner}")


#writing the output to the text file

path =r'C:\Users\rolis\OneDrive\Desktop\python_Homework\PyPoll\Analysis\election_data.txt' #path of the output file

with open(path,'w') as f:
    f.write("Election Results")
    f.write('\n')
    f.write("----------------------")
    f.write('\n')
    f.write(f"Total Votes: {total_votes}")
    f.write('\n')
    f.write("-----------------------")
    f.write('\n')
    for candidate, votes in candidate_votes.items():
       f.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
       f.write('\n')
    
    f.write("-----------------------")
    f.write('\n')
    f.write(f"Winner:{winner}")
          
    


         