import pandas


data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

"""calculating average temp"""
# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(temp_list)
# print(average_temp)

# average_temp = data["temp"].mean()
# print(average_temp)

"""getting a column"""
# print(data.temp_list)
# print(data["temp"])

"""getting row"""
# print(data[data.day == "Monday"])


"""getting row of max temp"""
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])

"""CHALLANGE- convert monday's temp to fahrenheit"""
monday = data[data.day == "Monday"]
monday_temp = int(monday["temp"])
print(monday_temp)
monday_temp_fahrenheit = monday_temp * 9/5 + 32
print(monday_temp_fahrenheit)

"""creating data frame from scratch"""
# data_dict = {
#     'students':["amy","sandy",'bob'],
#     "scores": [65,45,86]
# }
# my_data = pandas.DataFrame(data_dict)
# print(my_data)

"""converting data to csv file"""

# my_data.to_csv("new_csv_file")