"""
author : Radka Prochazkova
email : radka-prochazkova@seznam.cz
discord: Radka P.

"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

line = "-" * 40
users = {"bob": "123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
       
while True:
    user_name = input("Username: ")
    if not user_name:
        print("Missing Username.")
        continue
    else:
        break

while True:
    password = input("Password: ")
    if not password:
        print("Missing Password.")
        continue
    else:
        break

if password == users.get(user_name):
    print("Welcome to the app " + user_name, "We have 3 texts to be analyzed.", sep="\n")
else: 
    print("Unregistered username, terminating the app.")
    exit()

print(line)

text_selection = input("Enter a number btw. 1 and 3 to select the text: ")

if text_selection.isnumeric():
        text_selection = int(text_selection)
        if text_selection < 1 or text_selection > 3:
            print("Invalid text number, terminating the app.")
            exit()
        else:
            chosen_text = TEXTS[text_selection - 1].split()
else:
    print("Invalid text number, terminating the app.")
    exit()

print(line)

# počet slov
words_count = {"words" : 0}
for word in chosen_text:
    if word not in words_count:
        words_count["words"] += 1
print("There are", words_count["words"], "words in the selected text.")

# počet slov začínajících velkým písmenem
title_case = {"words" : 0}
for word in chosen_text:
    if not word.isnumeric() and word.istitle():
        title_case["words"] += 1
print("There are", title_case["words"], "titlecase words.")

# počet slov psaných velkými písmeny
upper_case = {"words" : 0}
for word in chosen_text:
    if word.isalpha() and word.isupper():
        upper_case["words"] += 1
print("There are", upper_case["words"], "uppercase words.")

# počet slov psaných malými písmeny
lower_case = {"words" : 0}
for word in chosen_text:
    if not word.isnumeric() and word.islower():
        lower_case["words"] += 1
print("There are", lower_case["words"], "lowercase words.")

# počet čísel (ne cifer)
numeric_string = {"numbers" : 0}
for number in chosen_text:
    if number.isnumeric():
        numeric_string["numbers"] += 1
print("There are", numeric_string["numbers"], "numeric strings.")

# suma všech čísel (ne cifer) v textu
sum_numbers = [0]
for number in chosen_text:
    if number.isnumeric():
        sum_numbers.append(int(number))
        sum_2 = sum(sum_numbers)
print("The sum of all the numbers is", sum_2)

print(line)

print("{:<3}".format("LEN"),"|", "{:^20}".format("OCCURENCE"), "|NR.")

letters_count = []
for word in chosen_text:
    word_lenght = len(word.strip(".,"))
    letters_count.append(word_lenght)

clean_lenghts = {}
for number in letters_count:
    if number not in clean_lenghts:
        clean_lenghts[number] = 1
    else:
        clean_lenghts[number] = clean_lenghts[number] + 1
for key, value in sorted(clean_lenghts.items()):
    print("{:<3}".format(key),"|", "{:<20}".format("*" * value), "|", value)