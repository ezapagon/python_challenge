import os
import csv
from types import CoroutineType
from typing import Counter

csvpath = os.path.join('/Users/Edo/Resources/election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Read the header row first  
    csv_header = next(csvreader)
   
    Counter = 0
    VoterIDList = []
    CandidateList = []
    Winner = []

    for row in csvreader:
        VoterIDList.append(row[0])
        CandidateList.append(row[2])
        Counter= Counter + 1
Votes_Correy_count = CandidateList.count('Correy')
Votes_Khan_count = CandidateList.count('Khan')
Votes_Li_count = CandidateList.count('Li')
Votes_OTooley_count = CandidateList.count("O'Tooley")

Percentage_votes_Correy = Votes_Correy_count/Counter *100
Percentage_votes_Khan = Votes_Khan_count/Counter *100
Percentage_votes_Li = Votes_Li_count/Counter *100
Percentage_votes_OTooley = Votes_OTooley_count/Counter *100

print('Election Results')
print('----------------------------') 
print('Total Votes:'+ str(Counter)) 
print('----------------------------') 
print('Correy: '+ str(Percentage_votes_Correy) + ' %  (' + str(Votes_Correy_count) +')') 
print('Khan: '+ str(Percentage_votes_Khan) + ' %  (' + str(Votes_Khan_count)+')') 
print('Li: '+ str(Percentage_votes_Li) + ' %  (' + str(Votes_Li_count)+')') 
print("O'Tooley: " + str(Percentage_votes_OTooley) + ' %  (' + str(Votes_OTooley_count)+')')
print('----------------------------') 
print('Winner: ')  

output_path_pypoll = os.path.join('/Users/Edo/Resources/analysis/output_file_pypoll.csv')

with open(output_path_pypoll, 'w', newline='') as csvfile2:

    csvwriter2 = csv.writer(csvfile2, delimiter=',')


    csvwriter2.writerow(['Election Results'])
    csvwriter2.writerow(['----------------------------'])
    csvwriter2.writerow(['Total Votes:'+ str(Counter)])
    csvwriter2.writerow(['----------------------------'])
    csvwriter2.writerow(['Correy: '+ str(Percentage_votes_Correy) + ' %  (' + str(Votes_Correy_count) +')'])
    csvwriter2.writerow(['Khan: '+ str(Percentage_votes_Khan) + ' %  (' + str(Votes_Khan_count)+')'])
    csvwriter2.writerow(['Li: '+ str(Percentage_votes_Li) + ' %  (' + str(Votes_Li_count)+')'])
    csvwriter2.writerow(["O'Tooley: " + str(Percentage_votes_OTooley) + ' %  (' + str(Votes_OTooley_count)+')'])
    csvwriter2.writerow(['----------------------------'])
    csvwriter2.writerow(['Winner: Khan '])
    csvwriter2.writerow(['----------------------------'])
