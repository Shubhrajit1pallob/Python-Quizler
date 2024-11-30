from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=300)
        self.question_txt = self.canvas.create_text(150, 125, width=280, text="Some Question text", fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.config(background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=right_img, highlightthickness=0, command=self.right_btn_check)
        self.true_btn.grid(column=0, row=2)

        self.false_btn = Button(image=wrong_img, highlightthickness=0, command=self.wrong_btn_check)
        self.false_btn.grid(column=1, row=2)

        self.next_question()


        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_txt, text=q_text)
        else:
            self.canvas.itemconfig(self.question_txt, text="You have reached the end of the quiz. Well Done!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def right_btn_check(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def wrong_btn_check(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)

