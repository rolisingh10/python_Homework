import csv #importing the csv module
#importing statistics module for finding average
import statistics 


total_months = 0   #putting total months to zero
total_revenue = 0  #putting total revenue to zero



prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]

greatest_decrease = ["", 0]

monthtoMonthChange = []

revenue_changes = []





csvpath = r'C:\Users\rolis\OneDrive\Desktop\python_Homework\PyBank\Resouces\budget_data.csv'   
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) #skipping the header
    # Variables to Track



   # Loop through all the rows of data we collect for row in reader:
    for row in csvreader:

       # Calculate the totals
       total_months = total_months + 1
       total_revenue = total_revenue + int(row[1])
       # print(row)



       # Keep track of changes
       revenue_change = int(row[1]) - prev_revenue
       # print(revenue_change)



       # Reset the value of prev_revenue to the row I completed my analysis
       prev_revenue = int(row[1])
       # print(prev_revenue)



       # Determine the greatest increase
       if (revenue_change > greatest_increase[1]):
           greatest_increase[1] = revenue_change
           greatest_increase[0] = row[0]



       if (revenue_change < greatest_decrease[1]):
           greatest_decrease[1] = revenue_change
           greatest_decrease[0] = row[0]



       # Add to the revenue_changes list
       revenue_changes.append(int(row[1]))
    for i in range(len(revenue_changes)-1):

       monthlyChange = (revenue_changes[i+1] -revenue_changes[i])
       monthtoMonthChange.append(monthlyChange)

    averageChange = statistics.mean(monthtoMonthChange)
    



   # Set the Revenue average
      # revenue_avg = sum(revenue_changes) / len(revenue_changes)
    #revenue_avg = sum(revenue_changes) / len(revenue_changes)
   # Show Output
print()
print()
print()
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(total_revenue))

print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")")
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
print("Average Change is: $" + str(round(averageChange, 2)))



#writing csv file to a text file
path = r'C:\Users\rolis\OneDrive\Desktop\python_Homework\PyBank\Analysis\PyBank.txt'

with  open(r'C:\Users\rolis\OneDrive\Desktop\python_Homework\PyBank\Analysis\PyBank.txt','w') as f:
   f.write("Financial Analysis")
   f.write('\n')
   f.write("-------------------------") 
   f.write('\n')
   f.write("Total Months: " + str(total_months))
   f.write('\n')
   f.write("Total Revenue: " + "$" + str(total_revenue))
   f.write('\n')
   f.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")")
   f.write('\n')
   f.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
   f.write('\n')
   f.write("Average Change is: $" + str(round(averageChange, 2)))



   

    

    
          
  

