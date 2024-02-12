class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {next_question.text} (True/False)?: ')
        self.check_answer(user_answer, next_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print('you got it right!')
            self.score += 1
        else:
            print('you got it wrong')
        print(f"the answer was {question_answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print('=============================')