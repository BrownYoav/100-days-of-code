import csv
with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()
for numb in file2_data:
    numb = int(numb)
result = [int(element) for element in file2_data if element  in file1_data]
print(file2_data)

# result =[int(row) for row in data1 if int(row) in file2]

# Write your code above 👆

print(result)


