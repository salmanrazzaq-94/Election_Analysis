# Needed Data
#1. Total number of votes cast
#2. Complete list of candidates who received votes
#3. Total number of votes each candidate received
# 4. Percentage of votes each candidate received
# 5. Winner of the election based on popular

# Add dependencies
import csv
import os

# Assign a vaiable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate options and votes
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1

        # If the candidate doesn't match an existing candidate...
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
        # Increment vote count
        candidate_votes[candidate_name] += 1

# Using the open() function with the "W" mode we will write data to the file
with open(file_to_save, "w") as txt_file:
# Printthe final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine percentage of vote for each candidate
    #1. Iterate through candidate list
    for candidate_name in candidate_votes:
        #2. Retrieve vote count
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
    
        #4. Print the candidate and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print winning candidate's results to the terminal
    winning_candidate_summary = (
        f"------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

    
