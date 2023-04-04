#calculate average temperature
temp = []
numDays = int(input("How many number of days "))
for i in range(numDays):
    temp.append(int(input("Enter the temp ")))
average_temp = sum(temp)/len(temp)

for i in temp:
    if i > average_temp:
        print(f"{i} is greater than {average_temp}")