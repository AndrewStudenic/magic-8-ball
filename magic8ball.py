import random

def magic8ball(AnswerNumber):
    if AnswerNumber == 1:
        return 'It is certain.'
    elif AnswerNumber == 2:
        return 'Yes.'
    elif AnswerNumber == 3:
        return 'It is decidedly so.'
    elif AnswerNumber == 4:
        return 'Reply hazy, try again.'
    elif AnswerNumber == 5:
        return 'Ask again later.'
    elif AnswerNumber == 6:
        return 'Concentrate and ask again.'
    elif AnswerNumber == 7:
        return 'My reply is NO.'
    elif AnswerNumber == 8:
        return 'Outlook not so good.'
    elif AnswerNumber == 9:
        return 'Very doubtful.'

r = random.randint(1, 9)
goagain = 'y'
while goagain == 'y':
    print('You turn over the magic 8 ball, and it says...')
    print()
    print(magic8ball(random.randint(1, 9)))
    print()
    r = random.randint(1, 9)
    goagain = str(input('Would you like to go again? If so, press "y": '))
