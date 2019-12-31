import random

def get_secret_word(word_file="/usr/share/dict/words"):
    good_words = []
    with open(word_file) as f:
        for word in f:
            word = word.strip()
            if not word.isalpha():
                continue
            if len(word) < 5:
                continue
            if word[0].isupper():
                continue
            good_words.append(word)

    word = random.choice(good_words)
    return word.lower()
        
def hide_secret_word(secret_word, correct_letters):
    l= len(secret_word)
    word = ""
    for i in range(0, l):
        if secret_word[i] in correct_letters:
            word += secret_word[i]

        else:
            word += "_"

    return word

def turns(secret_word, correct_letters, wrong_letters, guess):
    c = False
    for i in secret_word:
        if i == guess:
            if i not in correct_letters:
                correct_letters += guess
            else:
                print("Already guessed")
            c = True

    if not c and guess.isalpha() and len(guess) == 1:
        if guess not in wrong_letters:
            wrong_letters += guess
        if guess in wrong_letters:
            print("Already guessed") 
        

    hidden_secret_word =hide_secret_word(secret_word, correct_letters)
    return [hidden_secret_word, correct_letters, wrong_letters]

##  state: 0 is dead , 1 is continue game, 2 is win
def dead_or_alive(secret_word= get_secret_word(), correct_letters="", wrong_letters="", guess=''):
        
    hidden_secret_word, correct_letters, wrong_letters =turns(secret_word, correct_letters, wrong_letters, guess)
   
    if len(wrong_letters) < 7:
        state = False
        message = "Word:"+hidden_secret_word

    else:
        state = True
        message = "You are dead"

    c = False
    for i in secret_word:
        if i not in correct_letters:
            c = False
            break
        else:
            c = True

    if c:
        state = True
        message = "You won"

    
    return [correct_letters, wrong_letters, state, message]

if __name__ == "__main__":
    game_over = False
    correct_letters  = ""
    wrong_letters = ""
    message = ""
    secret_word = get_secret_word()
    print("Word:", end = "")
    print(hide_secret_word(secret_word, ""))

    while not game_over:
        guess = input("Guess:")
        correct_letters, wrong_letters, game_over, message = dead_or_alive(secret_word, correct_letters, wrong_letters, guess)
        print(f"\n\nchances remaining:{7-len(wrong_letters)}")
        print(f"Guesses so far:{correct_letters+wrong_letters}")
        print(f"{message}")

    
