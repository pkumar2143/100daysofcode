class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list # Assume List of Question objects
        self.score = 0

    def next_question(self):
        current_question = self.question_list[ self.question_number ]
        self.question_number += 1
        print(f"Q.{self.question_number}. {current_question.text} \n")
        user_answer = input("([T]rue or [F]alse)? : ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list) # Starts at 0. Ends at index 11 for a total of 12 items.
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Right!")
            self.score += 1
        else:
            print("Wrong")
        
        print(f"\nCurrent score = {self.score}/{self.question_number}\n")
