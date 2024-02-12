from data import *
from question_model import Question
from quiz_brain import *

question_bank = []
for element in question_data:
    q_text = element['text']
    q_answer = element["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("you have completed the quiz")
print(f"your score was {quiz.score}/{quiz.question_number}")