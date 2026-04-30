# ──────────────────────────────────────────────
#  main_app.py  –  F.R.I.D.A.Y  Chatbot App
# ──────────────────────────────────────────────

from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import webbrowser
import pandas as pd
import pywhatkit
import datetime
import pyautogui
import time

import voice_recoginition
import speech_output


# ── Constants ─────────────────────────────────

FILE_NAME       = "chatbot_data.txt"
BOT_NAME        = "friday"
WEBBROWSER_LIST = ["google", "youtube", "facebook"]


# ── Data helpers ──────────────────────────────

def load_data():
    """Read all saved Q&A pairs from disk and return as a dict."""
    data = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                if "|" in line:
                    q, a = line.strip().split("|", 1)
                    data[q.lower()] = a
    return data


def save_data(q, a):
    """Append a single Q&A pair to the data file."""
    with open(FILE_NAME, "a") as file:
        file.write(f"\n{q}|{a}")


# ── Import from CSV / TXT ─────────────────────

def import_data_file():
    """Let the user pick a CSV or TXT file and bulk-import Q&A pairs."""
    global data

    file_path = filedialog.askopenfilename(
        title="Select Data File",
        filetypes=(("CSV Files", "*.csv"), ("Text Files", "*.txt")),
    )
    if not file_path:
        return

    try:
        count = 0
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
            for _, row in df.iterrows():
                q, a = str(row[0]).strip(), str(row[1]).strip()
                if q and a:
                    data[q.lower()] = a
                    save_data(q, a)
                    count += 1
        else:
            with open(file_path, "r") as file:
                for line in file:
                    if "|" in line:
                        q, a = line.strip().split("|", 1)
                        data[q.lower()] = a
                        save_data(q, a)
                        count += 1

        messagebox.showinfo("✅ Success", f"Imported {count} Q&A pairs from:\n{file_path}")
    except Exception as e:
        messagebox.showerror("❌ Error", f"Failed to import data:\n{e}")


# ── Teaching window ───────────────────────────

# REPLACE the teach_bot function definition:
def teach_bot(question):
    """Open a small window so the user can teach the bot a new answer."""
    def save_answer():
        ans = ans_entry.get().strip()
        if ans:
            data[question.lower()] = ans
            save_data(question, ans)
            chat.insert(END, f"Bot learned: {ans}\n")
            speech_output.speak_text(f"I learned: {ans}")
            train_win.destroy()

    train_win = Toplevel(new_win)
    train_win.title("Teach F.R.I.D.A.Y")
    Label(train_win, text=f"Answer for: '{question}'", font=("Arial", 12, "bold")).pack(pady=5)

    ans_entry = Entry(train_win, width=40, font=("Arial", 12))
    ans_entry.pack(pady=5)

    Button(train_win, text="Save", command=save_answer, bg="green", fg="white").pack(pady=5)


# ── Send / message handler ────────────────────

def send():
    """Process the user's message and generate a bot response."""
    global user_msg
    user_msg = chat_entry.get().strip()

    if not user_msg:
        return

    chat.insert(END, f"You: {user_msg}\n")
    msg_lower = user_msg.lower()

    # Play a song on YouTube
    if "play" in msg_lower and "youtube" in msg_lower:
        try:
            song_name = msg_lower.replace("play", "").replace("on youtube", "").strip()
            if song_name:
                chat.insert(END, f"Bot: Playing {song_name}\n")
                speech_output.speak_text(f"Playing {song_name} on Youtube")
                pywhatkit.playonyt(song_name)
            else:
                chat.insert(END, "Bot: Please tell me which song you want to play on YouTube.\n")
                speech_output.speak_text("Please tell me which song you want to play on Youtube")
        except Exception as e:
            speech_output.speak_text("Sorry I didn't get you")
            print(e)

    # Known Q&A lookup
    elif msg_lower in data:
        reply = data[msg_lower]
        chat.insert(END, f"Bot: {reply}\n")
        speech_output.speak_text(reply)
        for url_name in WEBBROWSER_LIST:
            if url_name in msg_lower:
                webbrowser.open(f"www.{url_name}.com")

    # Tell current time
    elif "time" in msg_lower:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        reply = f"The current time is {now}."
        chat.insert(END, f"Bot: {reply}\n")
        speech_output.speak_text(reply)

    # Take a screenshot
    elif "screenshot" in msg_lower:
        try:
            chat.insert(END, "Bot: Taking screenshot in 5 seconds. Minimize the window now!\n")
            speech_output.speak_text("Taking screenshot in five seconds")
            time.sleep(5)
            ss = pyautogui.screenshot()
            ss.save("friday_screenshot.png")
            reply = "Screenshot taken and saved as 'friday_screenshot.png'!"
            chat.insert(END, f"Bot: {reply}\n")
            speech_output.speak_text(reply)
        except Exception as e:
            chat.insert(END, f"Bot: Failed to take screenshot: {e}\n")

    # Check if user database exists
    elif "check database" in msg_lower:
        if os.path.exists("user_details.txt"):
            reply = "Database file is present and secure."
        else:
            reply = "Warning: The user database file is missing!"
        chat.insert(END, f"Bot: {reply}\n")
        speech_output.speak_text(reply)

    # Google search
    elif "search" in msg_lower:
        query = msg_lower.replace("search", "").strip()
        if query:
            reply = f"Searching Google for {query}..."
            chat.insert(END, f"Bot: {reply}\n")
            speech_output.speak_text(reply)
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            chat.insert(END, "Bot: What would you like me to search for?\n")

    # Unknown — ask user to teach the bot
    else:
        chat.insert(END, "Bot: I don't know that. Please teach me!\n")
        speech_output.speak_text("I don't know that. Please teach me!")
        teach_bot(user_msg)

    chat_entry.delete(0, END)


# ── Main GUI ──────────────────────────────────

def my_app_gui(name="User"):
    """Build and launch the F.R.I.D.A.Y chat window."""
    global chat_entry, chat, new_win

    # Window
    new_win = Tk()
    new_win.title("FRIDAY AI")
    new_win.geometry("1920x1080")
    new_win.config(bg="black")

    # Header logo + title
    chat_bot_img = Image.open("friday_ai.png")
    chat_bot_img = chat_bot_img.resize((200, 120))
    final_image = ImageTk.PhotoImage(image=chat_bot_img)

    Label(
        new_win,
        image=final_image,
        text="F.R.I.D.A.Y",
        compound=LEFT,
        font=("Arial", 30, "bold"),
        fg="#00FFFF",
        bg="black",
    ).pack()

    # Chat area
    chat_frame = Frame(new_win, width=80, bg="black")
    chat_frame.pack()

    chat = Text(
        chat_frame,
        width=80,
        height=15,
        font=("Arial", 15, "bold"),
        fg="white",
        bg="black",
    )
    chat.pack(pady=20)

    # User icon
    user_img = Image.open("user.png")
    user_img = user_img.resize((40, 40))
    user_photo = ImageTk.PhotoImage(user_img)

    user_icon_label = Label(chat_frame, image=user_photo, bg="black")
    user_icon_label.image = user_photo
    user_icon_label.pack(side=LEFT, padx=5)

    # Text input
    chat_entry = Entry(chat_frame, width=40, font=("Arial", 13, "bold"))
    chat_entry.pack(side=LEFT, padx=5)

    # Send button
    Button(
        chat_frame,
        text="Send",
        command=send,
        font=("Times New Roman", 13, "bold"),
        width=10,
        fg="white",
        bg="green",
    ).pack(side=LEFT)

    # Voice input
    def voice_input():
        voice_text = voice_recoginition.recognize_voice()
        if voice_text:
            voice_text = voice_text.lower()
            if BOT_NAME in voice_text:
                command = voice_text.replace(BOT_NAME, "").strip()
                chat_entry.delete(0, END)
                chat_entry.insert(0, command)
                send()
            else:
                print(f"Ignored: Did not hear '{BOT_NAME}'")

    Button(
        chat_frame,
        text="MIC",
        command=voice_input,
        font=("Times New Roman", 13, "bold"),
        width=12,
        fg="white",
        bg="red",
    ).pack(side=LEFT, padx=5)

    # Upload data button
    Button(
        chat_frame,
        text="Upload Data",
        command=import_data_file,
        font=("Times New Roman", 13, "bold"),
        width=12,
        fg="white",
        bg="blue",
    ).pack(side=LEFT, padx=5)

    # Greeting
    formatted_name = name.capitalize()
    greeting = f"Online and ready, {formatted_name}. How can I assist you today?"
    chat.insert(END, f"Bot: {greeting}\n")
    speech_output.speak_text(greeting)

    new_win.mainloop()


# ── Startup ───────────────────────────────────

data = load_data()

# Uncomment to test directly without login:
# my_app_gui()