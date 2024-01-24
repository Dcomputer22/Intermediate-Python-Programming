import pandas

nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet_data.iterrows()}
print(nato_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters from alphabets are allowed!")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()