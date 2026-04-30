from tkinter import *
from tkinter import messagebox

def register_details(user_name,password,phone_num, email):
    if user_name!="" and password!="" and phone_num!="" and email!="":
        d = {"username":user_name, 
            "password":password,
            'phonenum':phone_num,
            'email':email}
        file = open("user_details.txt", mode='w')
        file.write(str(d))
        messagebox.showinfo("User Details Saved", "Save Done!")
        file.close()
        signup_root.destroy()
    else:
        messagebox.showerror("Blank detected", "Fill all the details and Try again")
        
    


def signup_page():
    global signup_root
    signup_root = Tk()
    signup_root.geometry("1920x1080")
    signup_root.config(bg="white")
    signup_root.title("Sign UP")

    # form position 
    main_frame = Frame(signup_root, bg="white")
    main_frame.place(relx=0.5, rely=0.5, anchor="center")


    heading_text = Label(
        main_frame, 
        compound=TOP,
        text="SIGN-UP HERE",
        fg="green",
        bg="white",
        font=("Arial", 32, "bold")
    )

    heading_text.pack(pady=20)

    #____________________________________________________________USERNAME_______________________________________________________________________________________________________________
    
    signup_user_frame = Frame(main_frame, bg='white')
    signup_user_frame.pack(pady=12)

    #user_name
    user_label= Label(signup_user_frame,
                    bg="white", 
                    text='Username',
                    fg="black",
                    font=('Arial',18,'bold'),
                    width=12,
                    anchor='e'
    )
    user_label.pack(side='left', padx=10)

    border = Frame(signup_user_frame, bg="black", padx=2, pady=2)
    border.pack(side=LEFT)

    signup_user_entry = Entry(border,fg="black",  relief=FLAT, font= ('Arial',20,'bold'),width=22)
    signup_user_entry.pack()

    # Password

    signup_pass_frame = Frame(main_frame, bg='white')
    signup_pass_frame.pack(pady=10)
    
    signup_pass_label= Label(signup_pass_frame,
                    bg="white", 
                    text='Password',
                    fg="black",
                    font=('Arial',18,'bold'),
                    width=12,
                    anchor='e'
    )

    signup_pass_label.pack(side='left', padx=10)

    border = Frame(signup_pass_frame, bg="black", padx=2, pady=2)
    border.pack(side=LEFT)

    signup_pass_entry = Entry(border, fg="black", relief=FLAT, font=('Arial',20,'bold'), width=22, show="*")
    signup_pass_entry.pack()
    
    # Phone number

    phone_frame = Frame(main_frame, bg='white')
    phone_frame.pack(pady=10)
    
    phone_label= Label(phone_frame,
                    bg="white", 
                    text='Phone Number',
                    fg="black",
                    font=('Arial',18,'bold'),
                    width=12,
                    anchor='e'
    )
    phone_label.pack(side='left', padx=10)

    border = Frame(phone_frame, bg="black", padx=2, pady=2)
    border.pack(side=LEFT)

    phone_entry = Entry(border,fg="black", relief=FLAT, font= ('Arial',20,'bold'),width=22)
    phone_entry.pack()

    # Email 
    Email_frame = Frame(main_frame, bg='white')
    Email_frame.pack(pady=10)
    
    Email_label= Label(Email_frame,
                    bg="white", 
                    text='Email',
                    fg="black",
                    font=('Arial',18,'bold'),
                    width=12,
                    anchor='e'
    )
    Email_label.pack(side='left', padx=10)

    border = Frame(Email_frame, bg="black", padx=2, pady=2)
    border.pack(side=LEFT)

    email_entry = Entry(border,fg="black",  relief=FLAT, font= ('Arial',20,'bold'),width=22)
    email_entry.pack()

    # Button 
    btn_frame = Frame(main_frame, bg='white')
    btn_frame.pack(pady=10)

    btn_signup = Button(btn_frame,
                text="Create Account",
                command=lambda: register_details(
                    signup_user_entry.get(),
                    signup_pass_entry.get(),
                    phone_entry.get(),
                    email_entry.get()
                ),
                fg="white", bg='green',
                width=15, relief=FLAT,
                font=('Arial',15,'bold'))
    btn_signup.pack()


    signup_root.mainloop()