import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_data)

squirrel_fur_data_list = squirrel_data["Primary Fur Color"].to_list()
numb_gray_squirrel = squirrel_fur_data_list.count("Gray")
numb_black_squirrel = squirrel_fur_data_list.count("Black")
numb_cinnamon_squirrel = squirrel_fur_data_list.count("Cinnamon")
print(numb_gray_squirrel)
print(numb_black_squirrel)
print(numb_cinnamon_squirrel)
print(squirrel_fur_data_list)
new_squirrel_data_dict = {
    "Fur Color":["Gray","Black","Cinnamon"],
    "Count":[numb_gray_squirrel,numb_black_squirrel,numb_cinnamon_squirrel]
}
new_squirrel_data_var = pandas.DataFrame(new_squirrel_data_dict)
new_squirrel_data_var.to_csv("new_squirrel_data")