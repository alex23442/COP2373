import customtkinter as ctk

app = ctk.CTk()

app.geometry("400x400")

def interface1():

    frame = ctk.CTkFrame(app)

    frame.pack(fill="both", expand=True)

    label = ctk.CTkLabel(frame, text="Hello World")

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

    label = ctk.CTkLabel(frame, text="Hello ")

    label.pack(pady=30)

    user_email = ctk.CTkEntry(frame)

    user_email.pack(side="left", pady=10, padx=25)

    enter_button = ctk.CTkButton(frame,
                                 text="Enter",
                                 command=frame.destroy)

    enter_button.pack(side="right", pady=10, padx=25)





interface1()
app.mainloop()