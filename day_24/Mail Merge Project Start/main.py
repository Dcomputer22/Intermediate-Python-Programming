NAME = "[name]"
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    name_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_content = letter_file.read()
    for each_name in name_list:
        stripped_name = each_name.strip()
        new_letter = letter_content.replace(NAME, stripped_name)

        with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as finished_letters:
            finished_content = finished_letters.write(new_letter)