import pandas
phonetic = pandas.read_csv("phonetic_alphabet.csv")
df = {row.letter: row.code for index,row in phonetic.iterrows()}

answer = input("Type a word you want. : ").upper()
answer_letter = [letter for letter in answer if answer.isalpha()]
answer_phonetic = {print(f"{letter} for {df[letter]}") for letter in answer_letter}

