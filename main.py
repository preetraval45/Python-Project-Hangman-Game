import random
from collections import Counter

# List of countries and cities
someWords = '''Afghanistan Albania Algeria Andorra Angola Argentina Armenia Australia Austria 
Azerbaijan Bahamas Bahrain Bangladesh Barbados Belarus Belgium Belize Benin Bhutan Bolivia 
Bosnia Botswana Brazil Brunei Bulgaria Burkina Faso Burundi Cambodia Cameroon Canada Chad Chile 
China Colombia Comoros Congo Costa Rica Croatia Cuba Cyprus Czech Republic Denmark Djibouti 
Dominica Ecuador Egypt El Salvador Eritrea Estonia Ethiopia Fiji Finland France Gabon Gambia 
Georgia Germany Ghana Greece Grenada Guatemala Guinea Guyana Haiti Honduras Hungary Iceland India 
Indonesia Iran Iraq Ireland Israel Italy Jamaica Japan Jordan Kazakhstan Kenya Kiribati Korea 
Kosovo Kuwait Kyrgyzstan Laos Latvia Lebanon Lesotho Liberia Libya Lithuania Luxembourg Madagascar 
Malawi Malaysia Maldives Mali Malta Marshall Islands Mauritania Mauritius Mexico Micronesia Moldova 
Monaco Mongolia Montenegro Morocco Mozambique Myanmar Namibia Nauru Nepal Netherlands New Zealand 
Nicaragua Niger Nigeria Norway Oman Pakistan Palau Panama Papua New Guinea Paraguay Peru Philippines 
Poland Portugal Qatar Romania Russia Rwanda Saint Lucia Samoa San Marino Saudi Arabia Senegal Serbia 
Seychelles Singapore Slovakia Slovenia Solomon Somalia South Africa Spain Sri Lanka Sudan Suriname 
Sweden Switzerland Syria Taiwan Tajikistan Tanzania Thailand Togo Tonga Tunisia Turkey Turkmenistan 
Tuvalu Uganda Ukraine UAE UK USA Uruguay Uzbekistan Vanuatu Vatican Venezuela Vietnam Yemen Zambia 
Zimbabwe'''

someWords = someWords.split(' ')
# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords).lower()

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a country or city')

    for i in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()

    playing = True
    # List for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:  # Flag is updated when the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: ')).lower()
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess  # The guessed letter is added as many times as it occurs

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif Counter(letterGuessed) == Counter(word):
                    # the game ends, even if chances remain
                    print("\nThe word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # To break out of the for loop
                    break  # To break out of the while loop
                else:
                    print('_', end=' ')

        # If user has used all of his chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
