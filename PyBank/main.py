import os
import csv

# join paths
csvpath = os.path.join("resources", "budget_data.csv")

# set variables
counter = 0
net_profit = 0 

# open/read csv
with open(csvpath, newline ="") as file_data:
    
# converting to readable data
    reader = csv.reader(file_data, delimiter=",")
    
# skip header row
    header = next(reader)
    
# create lists for storing profit and months
    p = []
    m = []

    for row in reader:
        counter = counter + 1
        net_profit = net_profit + int(row[1])
        p.append(int(row[1]))
        m.append(row[0])
        
    change = []

    for i in range(1, len(p)):
        change.append((int(p[i]) - int(p[i - 1])))
    
    average = sum(change) / len(change)
    
    increase = max(change)

    decrease = min(change)
    
    months = len(m)

    print("Analyis")
    print("........................................................")
    print("Total months: " + str(months))
    print("Total: $" + str(net_profit))
    print("Average change: $" + str(average))
    print("Greatest Increase in Profits: " + str(m[change.index(max(change))+1]) + " " + "$" + str(increase))
    print("Greatest Decrease in Profits: " + str(m[change.index(min(change))+1]))

file = open("exported_data.txt", "w")
file.write("Analyis")
file.write("\n--------------------------------------------------------------")
file.write("\nTotal months: " + str(months))
file.write("\nTotal: $" + str(net_profit))
file.write("\nAverage change: $" + str(average))
file.write("\nGreatest Increase in Profits: " + str(m[change.index(max(change))+1]) + " " + "$" + str(increase))
file.write("\nGreatest Decrease in Profits: " + str(m[change.index(min(change))+1]) + " " + "$" + str(decrease))
file.close()





 