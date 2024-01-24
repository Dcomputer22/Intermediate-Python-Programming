import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# data_list = data["temp"].to_list()
# average = sum(data_list) / len(data_list)
# print(average)
#OR
# average = data["temp"].mean()
# print(average)
# maximum_temp = data["temp"].max()
# print(maximum_temp)
# print(data["condition"]) # Or print(data.collection)

#Get Data Row
# print(data[data.day == 'Wednesday'])
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# temp_in_fah = (monday_temp * 9 / 5) + 32
# print(temp_in_fah)

#Create a dataframe from scratch
# data_dict = {
#     "students": ["Amama", "Zainab", "Samad"],
#     "scores":[76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data_to_csv = data.to_csv("new_data.csv")

temper = data[data.temp == 14]
print(temper.temp)


