def new_game():
    guesses = []
    correct_guesses = 0
    question_no = 1
    for i in questions:
        print('-----------------------')
        print(i)
        for j in answers[question_no-1]:
            print(j)
        question_no += 1
        guess = input('Enter A/B/C/D: ').upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(i), guess)  

    display_score(correct_guesses, guesses)     

def check_answer(answer, guess):
    if answer == guess:
        print('Correct!')
        return 1
    else:
        print('Wrong!')
        return 0

def display_score(correct_guesses, guesses):
    print('-----------------------')
    print('Result:')
    print('-----------------------')
    print('Answers: ', end='')
    for i in questions:
        print(questions.get(i), end=' ')
    print()
    print('Guesses: ', end='')
    for i in guesses:
        print(i, end=' ') 
    print()       
    print(f'You have got {correct_guesses} points!')
        
def play_again():
    response = input('Do you Want to play again ? (y/n): ')
    response = response.upper()
    if response == 'Y':
        return True
    else:
        return False    


questions = {
    'Who created Python?: ': 'A',
    'What year was Python created: ': 'B',
    'Python is tributed to which dance company!': 'C',
    'Is the earth round?: ': 'A'
}

answers =  [['A. Guido van rossum', 'B. Bill gates', 'C. Elon Musk', 'D. Mark Zach'], ['A. 1989', 'B. 2016', 'C. 2000', 'D. 2001'],
['A. Lonely Island', 'B. B Smosh', 'C. Monty Python', 'D. SNL'], ['A. False', 'B. True', 'C. Sometimes', 'D. What is this!']]

new_game()
while play_again():
    new_game()
