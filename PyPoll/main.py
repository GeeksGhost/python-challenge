# Modules
import os
import csv

# set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Function to analyze the data in elections_data.csv 
def pypoll(election_data):


    # Set Variables
    total_votes = 0
    #ballot_id = []
    #county = []
    candidate_counts = {}
   
    for row in election_data:
        # Add ballot_id 
     #   ballot_id.append(row[0])

        #add county
      #  county.append(row[1])

        #add candidate
        candidate = row[2]

        # counts the total votes 
        total_votes += 1 

        if(candidate in candidate_counts):
            candidate_counts[candidate] = candidate_counts[candidate] + 1
        else:
            candidate_counts[candidate] = 1
    

    
      
    # print and write to file "PyPollResults"
    with open("PyPollResults.txt", "w") as file:

        print("Election Results\n")
        file.write("Election Results\n")
        print("-------------------\n")
        file.write("-------------------\n")
        print("Total Votes: ", total_votes, "\n")
        file.write("Total Votes: "+ str(total_votes) + "\n")
        print("--------------------\n")
        file.write("--------------------\n")
    
        winner = ""
        winner_votes = 0 

        for key in candidate_counts:
            value = candidate_counts[key]
            print(key + ": " + str(value / total_votes * 100) + "% " + "(" + str(value) + ")" )
            file.write(str(key) + ": " + str(value / total_votes * 100) + "% " + "(" + str(value) + ")")

        if value > winner_votes:
            winner = key
            winner_votes = value


        #print(candidate_counts[key] / total_votes * 100)
        print("\n------------------\n")
        file.write("\n------------------\n")
        print("Winner: " + winner + "\n")
        file.write("Winner: " + winner + "\n")
        print("------------------\n")
        file.write("------------------\n")
    
    # write to a file "PyPollResults"


# Open the CSV file
with open(csvpath, encoding="utf8") as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # Skip the header row
    next(csvreader)

    # Call the pypoll function
    pypoll(csvreader)
