from hangman import get_secret_word
from hangman import hide_secret_word
from hangman import turns
from hangman import dead_or_alive
#from hangman import main


def test_secret_word_no_punctuation():
    with open("/tmp/words.txt","w") as f:
        for i in ["word'one", "word_two", "wordthree"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "wordthree"

def test_secret_word_atleast_five():
    with open("/tmp/words.txt","w") as f:
        for i in ["wo", "wor", "word", "bigword"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "bigword"

def test_secret_word_lowercase():
    with open("/tmp/words.txt","w") as f:
        for i in ["Wording", "wOrding", "WORDING", "wording"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "wording"

def test_secret_word_no_repeat():
    with open("/tmp/words.txt","w") as f:
        for i in ["disaster","recall","advise","national","infrastructure","shots","fired", "federation", "duress"]:
            f.write(i+"\n")
    l = []
    for i in range(3):
        l.append(get_secret_word('/tmp/words.txt'))
    assert len(set(l)) == 3


    
def test_hide_secret_word_no_input():
    assert hide_secret_word("memory", "") == "______"

def test_hide_secret_word_single_guess():
    assert hide_secret_word("memory","m'") == "m_m___"

def test_hide_secret_word_two_guesses():
    assert hide_secret_word("mammal", "ml") == "m_mm_l"

def test_hide_secret_word_full_guessed():
    assert hide_secret_word("sandal", "sndla") == "sandal"


def test_turns_right_guess():
    secret_word = "mammal"
    correct_letters = ""
    wrong_letters = ""
    guess_letter = 'a'
     
    assert turns(secret_word, correct_letters, wrong_letters, guess_letter) == ["_a__a_","a", ""]


def test_turns_wrong_guess_repeat():
    secret_word = "mammal"
    correct_letters = "am"
    wrong_letters = "ef"
    guess_letter = 'e'
     
    assert turns(secret_word, correct_letters, wrong_letters, guess_letter) == ["mamma_", "am", "ef"] 

def test_turns_right_guess_repeat():
    secret_word = "mammal"
    correct_letters = "am"
    wrong_letters = "ef"
    guess_letter = 'a'
     
    assert turns(secret_word, correct_letters, wrong_letters, guess_letter) == ["mamma_", "am", "ef"] 
    

def test_turns_with_wrong_guess():
    secret_word = "mammal"
    correct_letters = "am"
    wrong_letters = "ef"
    guess_letter = 'g'
     
    assert turns(secret_word, correct_letters, wrong_letters, guess_letter) == ["mamma_", "am", "efg"]  

def test_turns_with_invalid_guess1():
    secret_word = "mammal"
    correct_letters = "am"
    wrong_letters = "ef"
    guess_letter = '1'
     
    assert turns(secret_word, correct_letters, wrong_letters, guess_letter) == ["mamma_", "am", "ef"]  



def test_turns_with_invalid_guess2():
    secret_word = "mammal"
    correct_letters = "am"
    wrong_letters = "ef"
    guess_letter = 'ef'
     
    assert turns(secret_word, correct_letters, wrong_letters, guess_letter) == ["mamma_", "am", "ef"] 


def test_dead_or_alive_wrong_guess_continue():
    secret_word = "mammal"
    correct_letters = "am"
    wrong_letters = "efg"
    guess = 'h'
## 0 is dead , 1 is continue game, 2 is win
    assert dead_or_alive(secret_word, correct_letters, wrong_letters, guess) == ["am", "efgh", False, "Word:mamma_"]
    
def test_dead_or_alive_right_guess_continue():
    secret_word = "mammal"
    correct_letters = "a"
    wrong_letters = "efg"
    guess = 'm'
## 0 is dead , 1 is continue game, 2 is win
    assert dead_or_alive(secret_word, correct_letters, wrong_letters, guess) == ["am", "efg", False, "Word:mamma_"]
    
def test_dead_or_alive_die():
    secret_word = "mammal"
    correct_letters = "am"
    wrong_letters = "efghij"
    guess = 'k'
## 0 is dead , 1 is continue game, 2 is win
    assert dead_or_alive(secret_word, correct_letters, wrong_letters, guess) == ["am", "efghijk", True, "You are dead"]
    

    
def test_dead_or_alive_win():
    secret_word = "mammal"
    correct_letters = "am"
    wrong_letters = "efg"
    guess = 'l'
## 0 is dead , 1 is continue game, 2 is win
    assert dead_or_alive(secret_word, correct_letters, wrong_letters, guess) ==  ["aml", "efg", True,"You won"]
    
    
    


    
