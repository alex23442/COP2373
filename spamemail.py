#TODO add comments, finish all interfaces.
import customtkinter as ctk

app = ctk.CTk()

app.geometry("400x400")

spam_words = {
    "money": 5,
    "fast": 5,
    "guaranteed": 10,
    "returns": 5,
    "profit": 5,
    "double": 5,
    "income": 5,
    "rich": 5,
    "million": 10,
    "dollars": 5,
    "cash": 5,
    "financial": 5,
    "freedom": 5,
    "act": 5,
    "now": 5,
    "last": 5,
    "chance": 5,
    "immediate": 5,
    "response": 5,
    "required": 5,
    "limited": 5,
    "time": 5,
    "hurry": 5,
    "expires": 5,
    "today": 5,
    "final": 5,
    "call": 5,
    "free": 10,
    "winner": 10,
    "unbelievable": 10
}


def interface1():

    frame = ctk.CTkFrame(app)

    frame.pack(fill="both", expand=True)

    label = ctk.CTkLabel(frame, text="Do you want to send a message?")

    label.pack(pady=30)

    yes = ctk.CTkButton(frame,
                        text="Yes",
                        command=lambda: (frame.destroy(), interface2()))

    yes.pack(side="left", pady=10, padx=25)

    no = ctk.CTkButton(frame,
                        text="no",
                        command=frame.destroy)


    no.pack(side="right", pady=10, padx=25)

def interface2():

    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)

    label = ctk.CTkLabel(frame, text="Please enter your email.")

    label.pack(pady=30)

    user_email = ctk.CTkEntry(frame)

    user_email.pack(side="left", pady=10, padx=25)

    enter_button = ctk.CTkButton(frame,
                                 text="Enter",
                                 command=lambda: interface3(user_email, frame))

    enter_button.pack(side="right", pady=10, padx=25)

def interface3(user_email,frame):

    useer = user_email.get()

    frame.destroy()

    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)

    label = ctk.CTkLabel(frame, text=useer)

    label.pack(pady=30)

    user_massage = ctk.CTkEntry(frame)

    user_massage.pack(side="bottom", pady=10, padx=25)

    command = interface4(user_massage)

def interface4(user_massage):
    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)

    user_massage = user_massage.get()

    score = 0

    while True:
        if user_massage == spam_words.get(user_massage):
            score += points

            print(score)

            label = ctk.CTkLabel(frame, text=score)

            label.pack(pady=30)







interface1()
app.mainloop()