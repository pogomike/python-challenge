import os
import csv

Votes = 0
dictionary = {}
Name = []
VoteCount = []
VotePrecentage = []
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    next(csvreader, None)
    
    # loop through range 1 to number of items in list
    for row in csvreader:
        #Total Votes
        Votes = Votes + 1
        #Create a dictionary of cantidates and their vote count
        if row[2] in dictionary.keys():
            dictionary[row[2]] = dictionary[row[2]] + 1
        else:
            dictionary[row[2]] = 1
            
    #Append the name of the cantidate and vote count to a list
    for key, value in dictionary.items():
        Name.append(key)
        VoteCount.append(value)

    #Append the precentage of votes to a list
    for i in VoteCount:
        i = round(((i/Votes) * 100),2)
        VotePrecentage.append(i)

    # Zip all three lists together into tuples
    middlelist = list(zip(Name, VoteCount, VotePrecentage))
    
print("----------------")
print("Election Results")
print("----------------")
print ("Total Votes:", Votes)
print("----------------")
for entry in middlelist:
        print(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')')
print("----------------")
print("Winner is: ", max(dictionary.items(), key = lambda x: x[1])[0])
print("----------------")

# Set variable for output file
output_file = os.path.join("pypoll.csv")

with open(output_file, 'w') as csvfile:
    csvfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(Votes))
    csvfile.writelines('\n-------------------------\n ')
    for entry in middlelist:
        csvfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ') \n ')  
    csvfile.writelines('-------------------------\n') 
    csvfile.writelines('Winner is: ' + max(dictionary.items(), key = lambda x: x[1])[0])