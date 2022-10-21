


class QuizBrain :
    def __init__(self, list):
        self.question_number =0 
        self.question_list = list
        self.score = 0
        
    def next_question(self):
        question_ask = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number } : {question_ask.text} (True/False) :")
        self.check_answer(user_ans,question_ask.answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower()  == correct_ans.lower():
            self.score +=1
            print("You got it right!")
        else:
            print("You got it wrong")
        print(f"The correct answer was : {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")