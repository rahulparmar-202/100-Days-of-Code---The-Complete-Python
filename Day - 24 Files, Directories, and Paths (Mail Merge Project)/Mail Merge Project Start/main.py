#TODO: Create a letter using starting_letter.txt 

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
#reading the names_file and storing in list (names)

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_content = letter_file.read()

    # looping through the names list
    for name in names:
        # strip removes un-necessary space, next-line etc.
        stripped_name = name.strip()
        # writing into the letter and replacing the "[name]" with the stripped_name
        new_letter = letter_content.replace(__old="[name]",__new=stripped_name)

        # when there's no file found , python creates new.
        output_file_path = f"./Output/ReadyToSend/letter_for_{stripped_name}.txt"
        with open(output_file_path, mode="w") as output_file:
            output_file.write(new_letter)
        # writing the new_letter into the output file
        print(f"Letter for {stripped_name} created.")





#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp