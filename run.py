import random
from random import shuffle

animals = ['cat','dog','horse']
countries = ['greece','italy', 'sweden']
food = ['pasta', 'rice', 'eggs']

print('Hello Tim! Ready to unscrable the word?\n')
print('You will be given words whose letters are scrambled.\n')
print('Your goal is to unscramble them and find the word.\n')
print('Please provide the number of the category of words you want to play with:\n')
print('1.Animals 2. Countries 3. Food\n')

def category_choice():
    number = int(input("Please enter a number:"))
    if number == 1:
        print('You chose "Animals"\n')
        print('Your scrambled word is:\n')
        unscrambled_word = random.choice(animals)
        l = list(unscrambled_word)
        shuffle(l)
        scrambled_word = ''.join(l)
        print(scrambled_word)

    if number == 2:
        print('You chose "Countries"\n')
        print('Your scrambled word is:\n')
        unscrambled_word = random.choice(countries)
        l = list(unscrambled_word)
        shuffle(l)
        scrambled_word = ''.join(l)
        print(scrambled_word)

    if number == 3:
        print('You chose "Food"\n')
        print('Your scrambled word is:\n')
        unscrambled_word = random.choice(food)
        l = list(unscrambled_word)
        shuffle(l)
        scrambled_word = ''.join(l)
        print(scrambled_word)

    """
    Raises error if the input is not of the correct type, in the correct order
    or does not have the correct length
    """
    players_guess = input("Unscramble here: ")

    try:
        if str(players_guess)!= str(unscrambled_word):
            raise ValueError(
                'The answer you provided is wrong'
            )
    except ValueError as e:
        print('Please try again.\n')


def main():
    """
    Calls all the functions
    """
    category_choice()

main()