import json
from difflib import get_close_matches

value = 5

data = json.load(open(
    "E:\\New folder (3)\\[FreeTutorials.Us] Udemy - the-python-mega-course\\08 Application 1 Building an Interactive "
    "Dictionary\\076 data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s ? If yes press Y else press N" % get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "The word is doesn't present.Please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "The word is doesn't present.Please double check it"


while value > 1:
    word = input("Enter the word")

    output = (translate(word))

    if type(output) == list:
        for i in output:
            print(i)
    else:
        print(output)
