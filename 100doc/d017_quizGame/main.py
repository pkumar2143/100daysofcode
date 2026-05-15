from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(text=entry['question'], answer=entry['correct_answer']) for entry in question_data] # Fancy stuff!
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You finished the quiz!")
print(f"\nYour final score is: {quiz.score}/{quiz.question_number}\n")