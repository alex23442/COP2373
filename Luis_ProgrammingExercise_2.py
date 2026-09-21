
#instead of doing regular Tkinter, I decided to do customtiknter because
#it allows me more options to customize the interfaces and make coding easier
import customtkinter as ctk


app = ctk.CTk()

app.geometry("400x400")

#this is my dictionary with a list of spam words
# and their point values.
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
    """
       Asks the user if they want to send a message or not.

       Parameters:
       None

       Variables:
       frame = creates a frame for the first interface
       label = creates a label that has a text on it that says "Do you want to send a message?"
       yes_button = creates a button that says "Yes" and has a command once pushed it moves onto interface 1.
       no_button = creates a button that says "no" and has a command once pushed destroys the current frame.


       Logic:
       1.Prompts the user with the question, "DO you want to send a message?"
       2.If user selects yes, they move onto the next interface.
       3.If user selects no it destroys the current frame.

       Return:
       None
       """

    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)

    #creates label with the question.
    label = ctk.CTkLabel(frame, text="Do you want to send a message?")
    label.pack(pady=30)

    #creates yes button with a command that destroy this frame but move onto the next interface
    yes_button = ctk.CTkButton(frame,
                        text="Yes",
                        command=lambda: (frame.destroy(), interface2()))
    yes_button.pack(side="left", pady=10, padx=25)

    #creates no button with a command that destroys this frame without moving onto the next one.
    no_button = ctk.CTkButton(frame,
                        text="no",
                        command=frame.destroy)
    no_button.pack(side="right", pady=10, padx=25)


def interface2():
    """
        Prompts the user to enter their email. Once they enter it and they
        press enter, they move to the next interface.

        Parameters:
        None

        Variables:
        frame = creates a frame for the second interface.
        label = creates a label asking the user to enter their email.
        user_email = stores the email entered by the user.
        enter_button = moves the user to the next interface.

        Logic:
        1.Promts the user to enter their email.
        2.Once they press enter, they move onto the next interface.

        Return:
        None
        """

    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)

    label = ctk.CTkLabel(frame, text="Please enter your email.")
    label.pack(pady=30)

    user_email = ctk.CTkEntry(frame)
    user_email.pack(side="left", pady=10, padx=25)

    #once this enter button is pressed, it passes the
    # user email and frame to interface3.
    enter_button = ctk.CTkButton(frame,
                                 text="Enter",
                                 command=lambda: interface3(user_email, frame))
    enter_button.pack(side="right", pady=10, padx=25)

def interface3(user_email,frame):
    """
        The user now has the option to write a message and send it.
        while they are typing, the spam detector gets updated in real time.

        Parameters:
        user_email = the email entered by the user.
        frame = the frame from the previous interface.

        Variables:
        user_email = stores the user's email.
        subject_message = stores the subject entered by the user.
        user_massage = stores the message entered by the user.

        Logic:
        1. Gets the email entered by the user.
        2. Destroys interface2.
        3. Creates interface3 for writing an email.
        4. The user enters a subject and message.
        5. The spam detector updates in real time.

        Return:
        user_massage, subject_message
        """
    #gets the email entered by the user.
    user_email = user_email.get()

    #destroys interface2
    frame.destroy()

    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)

    from_label = ctk.CTkLabel(frame, text=f"From:{user_email}")
    from_label.pack(anchor="w", pady=5, padx=25)

    to_label = ctk.CTkLabel(frame, text="To: United States of America")
    to_label.pack(anchor="w", pady=(15,5), padx=25)

    subject_label = ctk.CTkLabel(frame, text="Subject:")
    subject_label.pack(anchor="w", pady=(10, 5), padx=25)

    subject_message = ctk.CTkEntry(frame, width=350, placeholder_text="Subject")
    subject_message.pack(pady=10, padx=25, fill="x")

    user_massage = ctk.CTkTextbox(frame, width=350, height=150)
    user_massage.pack(pady=10, padx=25, fill="both", expand=True)


    #creates a send button that completely destroys
    #and withdraws from the screen interface3
    enter_button = ctk.CTkButton(frame,text="Send", command=lambda: (frame.destroy(), app.withdraw()))
    enter_button.pack(side="bottom", pady=10, padx=20 )

    #Passes the message and subject boxes to interface4
    #so the spam score can be updated in real time.
    interface4(user_massage, subject_message)

def interface4(user_massage, subject_message):
    """
           checks and updates in real time if the message being
           sent from the user is a spam or not.

           Parameters:
           user_massage = the message entered by the user.
           subject_message = the subject entered by the user.

           Variables:
           spam_window = creates a separate window for the spam score.
           score_label = displays the current spam score.
           status_label = displays whether the message is spam.

           Logic:
           1. Gets the subject and message from the user.
           2. Splits the subject and message into individual words.
           3. Checks each word against the spam_words dictionary.
           4. Adds the corresponding points to the spam score. 5. Updates the spam score and spam status.
           6. Repeats the process every 100 milliseconds.

           Return:
           None
           """
    spam_window = ctk.CTkToplevel(app)
    spam_window.geometry("300x250")
    spam_window.title("spam prevention")

    #displays the current spam score.
    score_label = ctk.CTkLabel(spam_window,text="Your spam score is:0 ")
    score_label.pack(pady=10)

    #displays whether the message is spam.
    status_label = ctk.CTkLabel(spam_window,text="Not spam")
    status_label.pack(pady=10)

    finish_button = ctk.CTkButton(
        spam_window,
        text="Finish",
        command=app.destroy)
    finish_button.pack(side="bottom", pady=10, padx=20)

    def update_spam():
        """
                checks and updates the spam score in real time.

                Parameters:
                massage = stores the message entered by the user.
                subject = stores the subject entered by the user.
                score = stores the current spam score.
                subject_words = stores the individual words from the subject.
                user_words = stores the individual words from the message.

                Variables:
                None

                Logic:
                1. Checks whether the message box still exists.
                2. Gets the current message and subject.
                3. Converts the message and subject to lowercase.
                4. Splits the message and subject into individual words.
                5. Checks each word against the spam_words dictionary.
                6. Adds the corresponding points to the spam score.
                7. Updates the spam score and spam status.
                8. Checks again after 100 milliseconds.

                Return:
                None
                """
        # Stops the function if the message box no longer exists.
        if not user_massage.winfo_exists():
            return

        # Gets the current message and subject.
        massage = user_massage.get('1.0', 'end')
        subject = subject_message.get()

        # Starts the spam score at zero.
        score = 0

        # Converts the subject and message to lowercase
        # and separates them into individual words.
        subject_words = subject.lower().split()
        user_words = massage.lower().split()

        # Checks each word in the subject against the spam_words dictionary.
        for word in subject_words:

            if word in spam_words:
                score += spam_words[word]

        # Checks each word in the message against the spam_words dictionary.
        for word in user_words:

            if word in spam_words:
                score += spam_words[word]

        # Updates the spam score displayed to the user.
        score_label.configure(text=f"spam score: {score}")

        # Determines the spam status based on the score.
        if score >= 20:
            status_label.configure(text=f"SPAM")


        elif score >= 10:
            status_label.configure(text=f"SUSPICIOUS")


        else:
            status_label.configure(text=f"NOT SPAM")

        # Runs the spam checker again after 100 milliseconds.
        spam_window.after(100, update_spam)

    # Starts the spam checker.
    update_spam()


interface1()
app.mainloop()