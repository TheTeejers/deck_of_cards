import random

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
suits = ['hearts', 'diamonds', 'clubs', 'spades']

cards = []
shuffleCards = []

def cardDeck():
    for i in range (0, len(values)):
        for k in range (0, len(suits)):
            singleCards = suits[k], values[i]
            cards.append(singleCards)
    print(cards)
    random.shuffle(cards)
    return cards



def shuffle(array):
    counter = len(array), temp, index


    while counter > 0:
        index = Math.floor(Math.random() * counter)
        counter -= 1
        temp = array[counter]
        array[counter] = array[index]
        array[index] = temp
    random.shuffle(array)
    print(temp)
    return array


random.shuffle(cardDeck())
