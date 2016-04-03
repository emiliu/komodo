import random

def returnRandomQuote():
    f = open('quotes.csv', 'r')
    quotes = []
    for line in f:
        quotes.append(line)
    output = random.choice(quotes).strip('\n')
    return output
    