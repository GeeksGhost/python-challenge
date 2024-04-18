# Modules
import os
import csv

# set path for file
csvpath = os.path.join("Resources", "budget_data.csv")


import csv

def pybank(budget_data):
    # list to store data
    total_months = 0
    net_total = 0
    count = 0
    difference = 0
    total_sum = 0 #sum of all changes
    previous_value = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_month = ""
    worst_month = ""
    
    # Iterate through each row in the CSV file
    for row in budget_data:
        # Increment total_months for each row
        total_months += 1

   # calculate the net total of profits/losses over the period
        profit_loss = float(row[1])
        net_total += profit_loss
        count += 1

        #changes.append(profit_loss)

    # calculate the average change in "profit/losses" over the entire period
        current_value = row[1]
        difference = int(current_value) - int(previous_value)
        previous_value = current_value
        total_sum += difference

        if difference > greatest_increase:
            greatest_increase = difference
            greatest_month = row[0]
        
        if difference < greatest_decrease:
            greatest_decrease = difference
            worst_month = row[0]

    average_difference = total_sum / total_months

    # Print 
    print ("Finanacial Analysis\n")
    print("--------------------------------------------\n")
    print("Total months:", total_months, "\n")
    print("Total: $" , net_total,"\n")
    print("Average Change: $", average_difference, "\n")
    print("Greatest Increase in Profits: " + greatest_month + " ($" + str(greatest_increase) + ")\n")
    print("Greatest Increase in Profits: " + worst_month + " ($" + str(greatest_decrease) + ")")
# Open the CSV file
with open(csvpath, encoding="utf8") as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # Skip the header row
    next(csvreader)

    # Call the pybank function
    pybank(csvreader)

    
        



    
