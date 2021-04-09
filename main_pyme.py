
import os
import csv
from typing import Counter

csvpath = os.path.join('/Users/Edo/Resources/budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Read the header row first  
    csv_header = next(csvreader)
    
    TotalProfitLosses = 0 
    Counter = 0
    ProfitLossesList = []

    for row in csvreader:
       ProfitLossesList.append(int(row[1]))
       ProfitLosses = row[csv_header.index('Profit/Losses')]
       

       TotalProfitLosses = TotalProfitLosses + int(row[1])
       Counter= Counter + 1

print('Financial Analysis')
print('----------------------------')   
print('Total Months:'+ str(Counter))   
print('Total:  $' + str(TotalProfitLosses))
print('Greatest Increase in Profits:  ' + str(max(ProfitLossesList)))
print('Greatest Decrease in Profits:  ' + str(min(ProfitLossesList)))

output_path = os.path.join('/Users/Edo/Resources/analysis/output_file.csv')

with open(output_path, 'w', newline='') as csvfile2:

    csvwriter = csv.writer(csvfile2, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Months:'+ str(Counter)])
    csvwriter.writerow(['Total:  $' + str(TotalProfitLosses)])
    csvwriter.writerow(['Greatest Increase in Profits:  ' + str(max(ProfitLossesList))])
    csvwriter.writerow(['Greatest Increase in Profits:  ' + str(min(ProfitLossesList))])