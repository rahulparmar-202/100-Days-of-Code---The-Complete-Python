capitals = {
    "India":"Delhi",
    "England":"London"
}

# Nested list in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# Pause - 1 (print Lille)
print(travel_log["France"][1])

# Pause - 2 (Print D)
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nested Dictionary
travel = {
    "India": {
        "Rajasthan":"Jaipur",
        "Maharashtra":"Mumbai"
    },
    "Uk": "London"
}

# Print Jaipur
print(travel["India"]["Rajasthan"])

# print Mumbai
print(travel["India"]["Maharashtra"])


# Pause - 3 print out "Stuttgart"
traveled = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

# print Stuttgart
print(traveled["Germany"]["cities_visited"][2])