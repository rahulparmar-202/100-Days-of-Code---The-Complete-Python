
import pandas

# opening and reading the main data csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250120.csv")

# counting the squirrels of each color
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# the new dict for the squirrels_data
new_data_dict = {
    "Fur Color":["gray","red","black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# converting to a DataFrame
new_data = pandas.DataFrame(new_data_dict)
# saving the new_data
new_data.to_csv("squirrels_data.csv")

# reading the squirrels_data.csv
squirrels = pandas.read_csv("squirrels_data.csv")
print(squirrels)