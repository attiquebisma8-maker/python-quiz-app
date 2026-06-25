import tkinter as tk
import random


class QuizApp:

    def __init__(self, window):

        self.window = window
        self.window.title("🧠 Advanced Python Quiz")
        self.window.geometry("550x450")
        self.window.configure(bg="#eaf4ff")


        self.questions = [

            {
                "q": "What is the output of print(type([]))?",
                "options": [
                    "list",
                    "<class 'list'>",
                    "array",
                    "tuple"
                ],
                "ans": "<class 'list'>"
            },

            {
                "q": "Which keyword is used to handle exceptions?",
                "options": [
                    "catch",
                    "try",
                    "error",
                    "except"
                ],
                "ans": "try"
            },

            {
                "q": "What does OOP stand for?",
                "options": [
                    "Object Oriented Programming",
                    "Open Object Program",
                    "Only Object Python",
                    "Operator Oriented Programming"
                ],
                "ans": "Object Oriented Programming"
            },

            {
                "q": "Which method runs when object is created?",
                "options": [
                    "__start__()",
                    "__init__()",
                    "create()",
                    "main()"
                ],
                "ans": "__init__()"
            },

            {
                "q": "Which data structure follows FIFO?",
                "options": [
                    "Stack",
                    "Queue",
                    "Tree",
                    "Dictionary"
                ],
                "ans": "Queue"
            },

            {
                "q": "Which type is immutable?",
                "options": [
                    "List",
                    "Dictionary",
                    "Set",
                    "Tuple"
                ],
                "ans": "Tuple"
            },

            {
                "q": "Which operator checks identity?",
                "options": [
                    "==",
                    "!=",
                    "is",
                    "in"
                ],
                "ans": "is"
            }

        ]


        random.shuffle(self.questions)

        self.index = 0
        self.score = 0


        self.title = tk.Label(
            window,
            text="🐍 PYTHON QUIZ",
            font=("Arial", 22, "bold"),
            bg="#eaf4ff",
            fg="#064789"
        )

        self.title.pack(pady=15)


        self.question_label = tk.Label(
            window,
            text="",
            font=("Arial", 15, "bold"),
            bg="#eaf4ff",
            fg="#064789",
            wraplength=450
        )

        self.question_label.pack(pady=20)



        self.answer = tk.StringVar()

        self.buttons = []


        for i in range(4):

            button = tk.Radiobutton(
                window,
                text="",
                variable=self.answer,
                value="",
                font=("Arial", 13),
                bg="white",
                fg="#064789",
                selectcolor="#bde0ff"
            )

            button.pack(pady=5)

            self.buttons.append(button)



        self.next_btn = tk.Button(
            window,
            text="NEXT ➜",
            command=self.next_question,
            font=("Arial", 12, "bold"),
            bg="#064789",
            fg="white",
            padx=25,
            pady=7
        )

        self.next_btn.pack(pady=20)


        self.show_question()



    def show_question(self):

        q = self.questions[self.index]

        self.question_label.config(
            text=q["q"]
        )


        for i in range(4):

            self.buttons[i].config(
                text=q["options"][i],
                value=q["options"][i]
            )


        self.answer.set("")



    def next_question(self):

        if self.answer.get() == self.questions[self.index]["ans"]:
            self.score += 1


        self.index += 1


        if self.index < len(self.questions):

            self.show_question()


        else:

            self.question_label.config(
                text=
                f"🎉 QUIZ COMPLETED 🎉\n\nScore: {self.score}/{len(self.questions)}"
            )


            for b in self.buttons:
                b.pack_forget()


            self.next_btn.config(
                text="DONE",
                state="disabled"
            )



root = tk.Tk()

app = QuizApp(root)

root.mainloop()