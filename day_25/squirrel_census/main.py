import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

total_gray = len(data[data["Primary_Fur_Color"] == "Gray"])

total_cinnamon = len(data[data["Primary_Fur_Color"] == "Cinnamon"])

total_black = len(data[data["Primary_Fur_Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [total_gray, total_cinnamon, total_black]
}

squirrel_data = pandas.DataFrame(squirrel_dict)
csv_file = squirrel_data.to_csv("squirrel_count")