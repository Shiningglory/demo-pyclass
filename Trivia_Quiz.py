import random
trivia_data = [
    {'question' : 'What is the capital of Nigeria?',
     'options' : ['Paris', 'Abuja', 'Lagos', 'Portharcourt'],
     'correct_answer' : 'Abuja'
    },
    {'question' : 'Who is the current president of Nigeria?',
     'options' : ['Muhammed Buhari', 'Atiku Abubakar', 'Peter Obi', 'Bola Tinubu'],
     'correct_answer' : 'Bola Tinubu'
    },
    {'question' : 'What is the largest mammal in the world?',
     'options' : ['Blue Whale', 'Elephant', 'Giraffe', 'Lion'],
     'correct_answer' : 'Blue Whale'
    },
    {'question' : 'Which planet is known as the Red Planet?',
     'options' : ['Mars', 'Earth', 'Jupiter', 'Venus'],
     'correct_answer' : 'Mars'
    },
    {'question' : 'Which gas do plants absorb from the atmosphere during photosynthesis?',
     'options' : ['Oxygen', 'Nitorgen', 'Carbon Dioxide', 'Hydrogen'],
     'correct_answer' : 'Carbon Dioxide'
    },
    {'question' : 'What is the biggest planet in our solar system?',
     'options' : ['Earth', 'Venus', 'Jupiter', 'Pluto'],
     'correct_answer' : 'Jupiter'
    },
    {'question' : 'What is the largest ocean on Earth?',
     'options' : ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Antarctica'],
     'correct_answer' : 'Pacific Ocean'
    },
    {'question' : 'Who wrote the play Romeo and Juliet?',
     'options' : ['Charles Dicksens', 'Chioma Achebe', 'William Shakespeare', 'Wole Soyinka'],
     'correct_answer' : 'William Shakespeare'
    },
    {'question' : 'Which year did Nigeria gain independence?',
     'options' : ['1950', '1860', '1850', '1960'],
     'correct_answer' : '1960'
    },
    {'question' : 'Who is the current president of USA?',
     'options' : ['Joe Biden', 'Donald Trump', 'Ebele Jonathan', 'Boris Johnnson'],
     'correct_answer' : 'Joe Biden'
    }
]

def ask_question(question_data):
    print(question_data['question'])
    for x, option in enumerate(question_data['options'], start= 1):
        print(f'{x}. {option}')
    player_answer = input('Enter the number of your answer:')
    if player_answer.isdigit():
        player_answer = int(player_answer)
        if 1 <= player_answer <= len(question_data['options']):
            if question_data['options'][player_answer - 1] == question_data['correct_answer']:
                return True
    return False

def play_game():
    score = 0
    random.shuffle(trivia_data)
    print('Welcome to the Trivia  Quiz Game!')
    for question_data in trivia_data:
        if ask_question(question_data):
            print('Correct!\n')
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question_data['correct_answer']}\n")
    print(f'Your final score is : {score}/ {len(trivia_data)}')

play_game()