
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
n = 0
while n < len(question_data):
    question_obj = Question(question_data[n]["text"],question_data[n]["answer"])
    question_bank.append(question_obj)
    n += 1

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {new_quiz.score}/{new_quiz.question_number}")


     