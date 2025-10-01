# Hindi-English Dictionary
# Simple program to translate Hindi words to English

words = {
    "billi": "cat",
    "bhains": "buffalo",
    "gadha": "donkey",
    "kutta": "dog"
}

word = input("Enter a Hindi word: ")

if word in words:
    print("English:", words[word])
else:
    print("Translation not found!")




  Example 1: Word exists in dictionary

Enter a Hindi word: billi
English: cat


Example 2: Word not in dictionary

Enter a Hindi word: sher
Translation not found!
