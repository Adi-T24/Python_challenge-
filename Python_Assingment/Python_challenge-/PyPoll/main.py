#Second half is to Analyze voter count respective of geography.

import csv
import os
# create a path to  "budget_data.csv"
output_path = os.path.join ('Python_challenge-\PyPoll\Resources\election_data.csv')
# Initialize variables
total_Votes = 0
candidates_Votes = {}
# Read the CSV file
with open('Python_challenge-\\PyPoll\\Resources\\election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    header = next(csvreader)
    # loop through the data
    for row in csvreader:
        # Count total votes
        total_Votes += 1
        # Count votes for each candidate
        candidate = row[2]
        if candidate in candidates_Votes:
            candidates_Votes[candidate] += 1
        else:
            candidates_Votes[candidate] = 1
# Calculate the percentage of votes each candidate won
candidates_percentages = {}
for candidate, votes in candidates_Votes.items():
    percentage = (votes / total_Votes) * 100
    candidates_percentages[candidate] = percentage
# Determine the winner based on popular vote
winner = max(candidates_Votes, key=candidates_Votes.get)
# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_Votes}")
print("-------------------------")
for candidate, votes in candidates_Votes.items():
    print(f"{candidate}: {candidates_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
# Export the results to a text file
with open('election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_Votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidates_Votes.items():
        output_file.write(f"{candidate}: {candidates_percentages[candidate]:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")