from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text_q = question["question"]
    ans = question["correct_answer"]
    new_q = Question(text_q,ans)
    question_bank.append(new_q)

# Object of QuizBrain class

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You Completed the quiz.")
print(f"Your final score was : {quiz.score}/{quiz.question_number}.")
