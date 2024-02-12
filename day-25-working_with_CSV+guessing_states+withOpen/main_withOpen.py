# with open(file="weather_data.csv") as file:
#     data = file.readlines()
# print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    teperatures = []
    for row in data:
        if 'temp' not in row:
            temp = int(row[1])
            teperatures.append(temp)
    print(teperatures)



