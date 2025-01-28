

# Example :- Try-except

# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# # except KeyError:
# #     print("got an Key Error.")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(f"from the file: {content}")
# finally:
#     # raise your error
#     raise KeyError("This is the error that i made up.")
    # file.close()
    # print("file closed.")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human heights should not be over 3 meters.")

bmi = weight / height ** 2
print(f"BMI : {bmi}")