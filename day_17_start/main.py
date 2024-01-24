from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain
question_bank = []
for each_question in question_data:
    question_text = each_question["question"]
    question_answer = each_question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz_Brain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz.")
print(f"Your final score was {quiz.score}/{len(question_bank)}")