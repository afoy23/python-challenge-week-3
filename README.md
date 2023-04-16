# python-challenge-week-3

PyBank
import os
import csv

#Path
path = "Resources/budget_data.csv"


# Variables 
Total_Months = 0
Total = 0
Value = 0
Average_Change = 0
Dates =[]
Profits = []

#Read CSV
csvfile = open(path)
csvreader = csv.reader(csvfile, delimiter =",")
csv_header = next (csvreader)
First_Row =next(csvreader)

Total_Months += 1
Total += int(First_Row[1])
Value = int(First_Row[1])

for row in csvreader:
    
    Dates.append(row[0])
    Average_Change = int(row[1])-Value
    Profits.append(Average_Change)
    Value = int(row[1])
    Total_Months += 1
    Total = Total + int(row[1])

    Avg_Chg = sum(Profits)/len(Profits)


#Greatest Increase & Decrease in Profits
Greatest_Increase = max(Profits)
Greatest_Decrease = min(Profits)
Increase_Index = Profits.index(Greatest_Increase)
Decrease_Index = Profits.index(Greatest_Decrease)
Increase_Date = Dates[Increase_Index]
Decrease_Date = Dates[Decrease_Index]


#Print
print(f"Financial Analysis")
print(f"----------------------------")
print(f'Total Months:{str(Total_Months)}')
print(f"Total:${str(Total)}")
print(f"Average Change: ${str(round(Avg_Chg,2))}")
print(f"Greatest Increase: {Increase_Date} (${str(Greatest_Increase)}")
print(f"Greatest Decrease: {Decrease_Date} (${str(Greatest_Decrease)}")

outputpath = "Financial Analysis/Financial_Analysis.csv"
# output_file = open ("Financial_Analysis") 
with open(outputpath, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    # row 1
    csvwriter.writerow(["Financial Analysis"])
    #row 2
    csvwriter.writerow(["----------------------------------"])
    #row 3 Total Months
    csvwriter.writerow([str(f"Total Months:{str(Total_Months)} ")])
    # row 4 Total 
    csvwriter.writerow([str(f"Total:{str(Total)} ")])
    # row 5 Total average 
    csvwriter.writerow([str(f"Average Change: ${str(round(Avg_Chg, 2))}")])
    #row 6 Greatest Increase In Profits
    csvwriter.writerow([str(f"Greatest Increase In Profits: {Increase_Date} (${str(Greatest_Increase)})")])
    #row 7 Greatest Decrease In Profits
    csvwriter.writerow([str(f"Greatest Decrease In Profits: {Decrease_Date} (${str(Greatest_Decrease)})")])
    
  PyPoll
  
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
