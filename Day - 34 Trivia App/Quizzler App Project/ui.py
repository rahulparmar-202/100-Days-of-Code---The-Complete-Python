
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, font=("Arial", 14, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=350, bg="white")
        self.question_text = self.canvas.create_text(
            150,125,
            width= 300,
            text="Questions goes here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_true)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_false)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    # display the questions on the screen (canvas)
    def get_next_question(self):
        # change the canvas bg to white again
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            # change the fill of question back to Theme_color
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            self.update_score() # update the score on the canvas
            q_text = self.quiz.next_question()
            # prints the question on the canvas
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You Completed the Quiz.", fill=THEME_COLOR)
            # disable the buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # when true button clicked
    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    # when the false button clicked
    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    # change the bg for 1sec and then get the next-question
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000,self.get_next_question,)


    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")