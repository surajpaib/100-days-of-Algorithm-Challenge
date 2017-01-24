
import random
import requests
import json

'''


'''


def words_api(word):
    response = requests.get("https://wordsapiv1.p.mashape.com/words/%s" %word,
                           headers={
                               "X-Mashape-Key": "WGOEGyk8g2mshvvUaLWGEzAEzr4bp1Jhr6gjsn6ECOIgDW6Dt0",
                               "Accept": "application/json"
                           }
                           )

    response_json=json.loads(response.text)

    word_meaning_e={}

    for word_meaning in response_json["results"]:
        try:

            word_meaning_e['synonyms']=word_meaning["synonyms"]
        except:

            word_meaning_e['synonyms'] = " "

        print("\n _________________________________________\n")
        print("Definition: %s" % word_meaning['definition'])
        print("")
        print("Part of Speech: %s" % word_meaning['partOfSpeech'])
        print("")
        print("Synonyms: %s" % word_meaning_e['synonyms'])

    return
'''


'''


def get_word():
    words = ["cheese", "president", "fire", "jingoism", "firebolt",
             "suffrage", "universal"]

    word_index = random.randint(0,len(words)-1)

    return words[word_index]
'''


'''


def get_blank_spaces(word):
    blank_space = "_" * len(word)
    for char in blank_space:
        print(char, ' ', end='')
    print("\n")
    return blank_space
'''


'''


def match_guess(word,blank_word,guess):
    input_letter = input("Enter your guess here")
    blank_word=list(blank_word)
    for i in range(0, len(word)):
        if word[i] == input_letter:
            blank_word[i] = input_letter
            guess = True

    return guess, blank_word


'''





'''


def wrong_guess(strike):
    strike_list=[]
    for count in range(strike):
        strike_list.append("--X--")
    strike_list_str='  '.join(strike_list)
    print(strike_list_str)
'''


'''


def play_word_game():
    word = get_word()
    blank_word = get_blank_spaces(word)

    playing = True

    strikes = 0
    while playing:

        guess = False
        guess, blank_word = match_guess(word, blank_word, guess)
        if guess:
            pass

        else:
            strikes += 1
            wrong_guess(strikes)

        if strikes >= 5:
            playing = False

        if blank_word == list(word):
            playing = False

        print_str='  '.join(blank_word)
        print(print_str, '  ', end='')
        print("\n")

    if strikes >= 5:
        print("\n")
        print("Sorry, you haven't guessed it right, the word is '%s'" % word)
        words_api(word)

    else:
        print("\n")
        print("You guessed it right!! Great Job")
        words_api(word)

'''


'''

play_word_game()





