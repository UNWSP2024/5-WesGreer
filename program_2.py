# Math Quiz Program
# Written by Wesley Greer on 2/17/2026

#define the function and the random numbers to add
import random
random_number1 = random.randint(1,500)
random_number2 = random.randint(1,500)

def math_quiz(n1,n2):
    answer = n1 + n2
    print('Solve this problem:')
    print(f'''
      {n1}  
    + {n2}
    ------''')
    return answer

# get user input and tell them if they are correct
answer = math_quiz(random_number1,random_number2)
user_answer = int(input('What is the answer? '))
if user_answer == answer:
     print('Correct! Nice job!')
else:
     print('Incorrect! The correct answer was', answer)
