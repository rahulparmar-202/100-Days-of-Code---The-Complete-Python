# CSV :- Comma Separated Values

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         # this if statement exclude the 'temp'
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

"""pandas.read_csv() :- to read a csv data file and store the formatted data"""
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data['temp'])

"""data_frame.to_dict() :- coverts the data_frame into a dictionary"""
# data_dict = data.to_dict()
# print(data_dict)

""".to_list() :- converts the data into a list format"""
# temp_list = data["temp"].to_list()
# print(temp_list)


"""challenge : calculate the avg temperature"""
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp.__round__(4))

"""using the .mean()"""
# print(data["temp"].mean())

"""maximum value from the temp"""
# print(data["temp"].max())

"""get Data in columns  (both are valid)"""
# print(data["condition"])
# print(data.condition)

""" Get Data in Row """
# print(data[data.day == "Monday"])
# will get the row of Monday


""" challenge : print the row of data which had highest temperature"""
# print(data[data.temp == data.temp.max()])

"get condition of Monday"
# monday = data[data.day == "Monday"]
# print(monday.condition)

"challenge: convert monday's temp into fahrenheit"
# monday_fah = (monday.temp[0]*9/5) + 32
# print(monday_fah)


""" Create a DataFrame from Scratch """
# data_dict = {
#     "students":["Amy", "James", "Harry","Peter"],
#     "scores":[97,82,89,94]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

