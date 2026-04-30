# ──────────────────────────────────────────────
#  login.py  –  Login screen for the chatbot app
# ──────────────────────────────────────────────

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import signup
import main_app
import ast


# ── Data ──────────────────────────────────────

user_details = {}


# ── Helpers ───────────────────────────────────

def load_user_details():
    """Load saved user credentials from disk into user_details."""
    global user_details
    if os.path.exists("./user_details.txt"):
        with open("./user_details.txt", "r") as file:
            user_details = ast.literal_eval(file.read())
        print(user_details)
    else:
        print("No user file found – cannot log in.")


# ── Button callbacks ──────────────────────────

def login_btn(username, password):
    """Validate credentials and open the main app on success."""
    global user_details

    if not username or not password:
        messagebox.showwarning("Blank Detected", "Kindly fill all the details.")
        return

    if not user_details:
        load_user_details()

    if username == user_details["username"] and password == user_details["password"]:
        messagebox.showinfo("Login Successful", "Welcome to the Project")
        root.destroy()
        main_app.my_app_gui(user_details["username"])
    else:
        messagebox.showerror("Login Unsuccessful", "Wrong username or password.")


def signup_btn():
    """Open the sign-up page."""
    signup.signup_page()


# ── Window setup ──────────────────────────────

root = Tk()
root.geometry("1920x1080")
root.title("Login Page")
root.config(bg="white")


# ── Logo / heading ────────────────────────────

img = Image.open("login_logo.png")
img = img.resize((200, 200))
photo_img = ImageTk.PhotoImage(img)

login_label = Label(
    root,
    compound=TOP,
    image=photo_img,
    text="Login Here",
    fg="green",
    bg="white",
    font=("Arial", 32, "bold"),
)
login_label.pack()


# ── Username row ──────────────────────────────

user_frame = Frame(root, bg="white")
user_frame.pack(pady=20)

Label(
    user_frame,
    text="Username",
    fg="blue",
    bg="white",
    font=("Arial", 20, "bold"),
).pack(side=LEFT, padx=20)

user_entry = Entry(
    user_frame,
    fg="black",
    bg="white",
    bd=5,
    relief=RAISED,
    font=("Arial", 20, "bold"),
)
user_entry.pack()


# ── Password row ──────────────────────────────

pass_frame = Frame(root, bg="white")
pass_frame.pack(pady=20)

Label(
    pass_frame,
    text="Password",
    fg="blue",
    bg="white",
    font=("Arial", 20, "bold"),
).pack(side=LEFT, padx=20)

pass_entry = Entry(
    pass_frame,
    fg="black",
    bg="white",
    bd=5,
    relief=RAISED,
    font=("Arial", 20, "bold"),
)
pass_entry.pack()


# ── Buttons ───────────────────────────────────

btn_frame = Frame(root, bg="white")
btn_frame.pack(pady=20)

Button(
    btn_frame,
    text="Login",
    command=lambda: login_btn(user_entry.get(), pass_entry.get()),
    fg="white",
    bg="green",
    bd=5,
    relief=RAISED,
    width=10,
    font=("Arial", 20, "bold"),
    activebackground="green",
    activeforeground="white",
).pack(side=LEFT, padx=50)

Button(
    btn_frame,
    text="Sign Up",
    command=signup_btn,
    fg="white",
    bg="red",
    bd=5,
    relief=RAISED,
    width=10,
    font=("Arial", 20, "bold"),
    activebackground="red",
    activeforeground="white",
).pack()


# ── Run ───────────────────────────────────────

root.mainloop()