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

    from_label = ctk.CTkLabel(frame, text=f"From:{useer}")
    from_label.pack(anchor="w", pady=5, padx=25)

    to_label = ctk.CTkLabel(frame, text="To: calel9334@gmail.com")
    to_label.pack(anchor="w", pady=(15,5), padx=25)

    subject_label = ctk.CTkLabel(frame, text="Subject:")
    subject_label.pack(anchor="w", pady=(10, 5), padx=25)

    subject_message = ctk.CTkEntry(frame, width=350, placeholder_text="Subject")
    subject_message.pack(pady=10, padx=25, fill="x")

    user_massage = ctk.CTkTextbox(frame, width=350, height=150)
    user_massage.pack(pady=10, padx=25, fill="both", expand=True)



    enter_button = ctk.CTkButton(frame,text="Send", command=lambda: (frame.destroy, app.withdraw()))
    enter_button.pack(side="bottom", pady=10, padx=20 )

    interface4(user_massage, subject_message)

def interface4(user_massage, subject_message):
    spam_window = ctk.CTkToplevel(app)
    spam_window.geometry("300x250")
    spam_window.title("spam prevention")

    score_label = ctk.CTkLabel(spam_window,text="Your spam score is:0 ")

    score_label.pack(pady=10)

    status_label = ctk.CTkLabel(spam_window,text="Not spam")
    status_label.pack(pady=10)

    def update_spam():

        if not user_massage.winfo_exists():
            return

        massage = user_massage.get('1.0', 'end')
        subject = subject_message.get()

        score = 0


        subject_words = subject.lower().split()
        user_words = massage.lower().split()

        for word in subject_words:

            if word in spam_words:
                score += spam_words[word]

        for word in user_words:

            if word in spam_words:
                score += spam_words[word]

        score_label.configure(text=f"spam score: {score}")

        if score >= 10:
            status_label.configure(text=f"SUSPICIOUS")

        elif score >= 20:
            status_label.configure(text=f"SPAM")


        else:
            status_label.configure(text=f"NOT SPAM")

        spam_window.after(100, update_spam)

    update_spam()









interface1()
app.mainloop()