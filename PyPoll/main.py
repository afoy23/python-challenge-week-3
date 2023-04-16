import os
import csv
# Path
path = 'Resources/election_data.csv'

# Variables
Candidates = []
Votes = []
Percent_Votes = []
Total_Votes = 0

# Read CSV
csvfile = open(path)
csvreader = csv.reader(csvfile, delimiter=",")
csv_header = next(csvreader)

for row in csvreader:
        
        Total_Votes += 1
        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            Votes.append(1)
        else:
            index = Candidates.index(row[2])
            Votes[index] += 1
    # Add to percent_votes list
for votes in Votes:
        percentage = (votes/Total_Votes) * 100
        percentage = "%.3f%%" % percentage
        Percent_Votes.append(percentage)

    # Find the winning candidate
winner = max(Votes)
index = Votes.index(winner)
winning_candidate = Candidates[index]

# printing the output
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(Total_Votes)}")
print("--------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(Percent_Votes[i])} ({str(Votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to text file
#Outputting to Election Analysis csv
outputpath = "Election Analysis/election_analysis.csv"
with open(outputpath, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([str(f"Total Votes:{str(Total_Votes)} ")])
    csvwriter.writerow(["----------------------------------"])
    for x in range(len(Candidates)):
        csvwriter.writerow([str(f"{Candidates[x]} {str(Percent_Votes[x])} ({str(Votes[x])})")])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([str(f"Winner:{str(winning_candidate)} ")])
    csvwriter.writerow(["----------------------------------"])

