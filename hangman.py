import random, os

word_list = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote',
'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama',
'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram',
'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger',
'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

hangman =[['   ________     ',
           '  |        |    ',
           '  |        |    ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '-----           '],
          ['   ________     ',
           '  |        |    ',
           '  |        |    ',
           '  |        0    ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '-----           '],
          ['   ________     ',
           '  |        |    ',
           '  |        |    ',
           '  |        0    ',
           '  |        |    ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '-----           '],
          ['   ________     ',
           '  |        |    ',
           '  |        |    ',
           '  |        0    ',
           '  |       /|    ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '-----           '],
          ['   ________     ',
           '  |        |    ',
           '  |        |    ',
           '  |        0    ',
           '  |       /|\   ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '-----           '],
          ['   ________     ',
           '  |        |    ',
           '  |        |    ',
           '  |        0    ',
           '  |       /|\   ',
           '  |        |    ',
           '  |             ',
           '  |             ',
           '  |             ',
           '  |             ',
           '-----           '],
          ['   ________     ',
           '  |        |    ',
           '  |        |    ',
           '  |        0    ',
           '  |       /|\   ',
           '  |        |    ',
           '  |         \   ',
           '  |             ',
           '  |             ',
           '  |             ',
           '-----           '],
          ['   ________     ',
           '  |        |    ',
           '  |        |    ',
           '  |        0    ',
           '  |       /|\   ',
           '  |        |    ',
           '  |       / \   ',
           '  |             ',
           '  |             ',
           '  |             ',
           '-----           ']]

gameEnd = False
current = 0
word = [i for i in random.choice(word_list).upper()]
guessed = []
for i in range(len(word)): guessed.append('  ')
check = [i for i in word]
incorrect = []

def play_again():
    global current, word, guessed, check, incorrect, gameEnd
    
    print('Would you like to play again (Y/N)\n>',end = '')
    cont = input().upper()
    
    if cont == 'Y':
        current = 0
        word = [i for i in random.choice(word_list).upper()]
        guessed = []
        for i in range(len(word)): guessed.append('  ')
        check = [i for i in word]
        incorrect = []
    else: gameEnd = True

def lastIndex(lst, value):
    i = len(lst)-1
    found = False
    while i >= 0 or found == False:
        if lst[i] == value:
            found = True
            return i
        else: i -= 1

def show_man():
    global current, guessed, word, incorrect
    
    os.system('cls')
    print(hangman[current][0])
    print(hangman[current][1])
    print(hangman[current][2])
    print(hangman[current][3])
    print(hangman[current][4])
    print(hangman[current][5])
    print(hangman[current][6])
    print(hangman[current][7])
    print(hangman[current][8])
    print(hangman[current][9])
    print(hangman[current][10])

    print('\nLives Left: '+str(7 - current))
    print('\n'+''.join(i for i in guessed))
    for i in range(len(word)): print('_ ',end = '')
    print('\n\nLetters Used:\n')
    print(' '.join(i for i in incorrect))
    print('\nGuess a Letter!\n>',end = '')

os.system('color c')
print('HANGMAN\n___________\n')
print('''Instructions: Try to figure out what word the PC is thinking of. Type in a letter to guess.
But be careful, you only have a certain number of guesses.\n\n''')
print('Type START to begin\n>', end = '')
start = input().upper()
if start != 'START':
    while start != 'START':
        print('you\'re suppose to type START not '+start+'\n>',end = '')
        start = input().upper()

while gameEnd == False:

    show_man()
    guess = input().upper()

    if len(guess) == 1:
        if guess in check:
            check.remove(guess)
            if guess in guessed:
                index = lastIndex(word, guess)
                guessed[index] = guess+' '
            else:
                index = word.index(guess)
                guessed[index] = guess+' '
        else:
            incorrect.append(guess)
            current += 1
    else:
        while len(guess) != 1:
            print('You can only enter one letter at a time\n>', end = '')
            guess = input().upper()

    if len(check) == 0 and current < 7:
        show_man()
        print('CONGRATULATIONS YOU GUESSED IT!')
        play_again()
    elif current == 7:
        show_man()
        print('The word was '+''.join(i for i in word))
        play_again()
        
    













































