import os
import csv
from operator import itemgetter

months = 0
revenue = 0
changeinmonth = []
monthChanges = []

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#budget_data
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # read CSV file & load into list
    CSVlist = list(csvreader)
    #Total Months
    months = len(CSVlist) - 1
    # loop through range 1 to number of items in list
    for row in range(1, len(CSVlist)):

        #Total Revenue
        revenue = revenue + int(CSVlist[row][1])
    
    # loop through range 1 to number of items in list less one
    for row in range(1, len(CSVlist)-1):
        # First Month of Revenue
        month1 = int(CSVlist[row][1])
        # Next Month of Revenue
        month2 = int(CSVlist[row+1][1])
        # Append the result of Month 2 - Month 1 to "Change in Month" List
        delta = month2-month1
        changeinmonth.append(delta)
        # declaring successor month to variable
        monthName = CSVlist[row+1][0]
        # declaring dictionary of month and delta 
        monthData = { "month" : monthName, "delta" : delta}
        # Append dictionary to list
        monthChanges.append(monthData)
    
    # The average change in "Profit/Losses" between months over the entire period
    avemonth = round(sum(changeinmonth)/(months-1), 2)
    
    # sort the list of dictionary by the property 'delta' 
    monthChanges = sorted(monthChanges, key=itemgetter('delta'))
    first = monthChanges[0]
    last = monthChanges[-1]

print("Financial Analysis")
print("--------------------------")
print ("Total Months:", months)
print ("Total Revenue: $" + str(revenue))
print ("Average Revenue Change: $" + str(avemonth))   
print ("Greatest Increase in Profits: " + last["month"] + "($" + str(last["delta"]) + ")")  
print ("Greatest Decrease in Profits: " + first["month"] + "($" + str(first["delta"]) + ")") 
 

# Set variable for output file
output_file = os.path.join("pybank.csv")

with open(output_file, 'w') as csvfile:
    csvfile.writelines('Financial Analysis \n------------------------- \nTotal Months: ' + str(months) +
     '\nTotal Revenue: $' + str(revenue) + '\nAverage Revenue Change: $' + str(avemonth) + 
     '\nGreatest Increase in Profits: ' + last["month"] + " ($" + str(last["delta"]) + ")" + 
     '\nGreatest Decrease in Profits: ' + first["month"] + " ($" + str(first["delta"]) + ")" )

     