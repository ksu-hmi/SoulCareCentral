from tkinter import *
import math
import time
import random
import datetime
import tkinter.simpledialog as simpledialog
import os
from PIL import Image, ImageTk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 0
timer = None

# ---------------------------- REMINDER MESSAGES ------------------------------- #
reminder_messages = [
    "🧘 Time to stretch your arms and legs!",
    "💧 Drink a glass of water!",
    "🌬️ Take 3 deep breaths.",
    "🚶‍♀️ Walk around for a minute.",
    "📴 Close your eyes, unclench your jaw, and relax your shoulders."
]

# ---------------------------- FUNCTION DEFINITIONS ------------------------------- #
def get_random_pose_image():
    poses_folder = "stretch_poses"
    pose_files = os.listdir(poses_folder)
    random_pose = random.choice(pose_files)
    pose_path = os.path.join(poses_folder, random_pose)

    pose_image = Image.open(pose_path)
    resized_pose = pose_image.resize((200, 224))
    tk_pose_image = ImageTk.PhotoImage(resized_pose)

    return tk_pose_image, random_pose

def get_random_prompt():
    prompts = [
        "What are you grateful for today?",
        "What is something you’re proud of recently?",
        "Describe how you feel right now in three words.",
        "What would make today great?",
        "What is one small act of kindness you can do?"
    ]
    return random.choice(prompts)

#Journal prompt
def prompt_journal_entry():
    question = get_random_prompt()
    entry = simpledialog.askstring("Journal Time 🖊️", question)
    if entry:
        mood = simpledialog.askstring(
            "Mood Tracker 💬",
            "How are you feeling?\nOptions:\nHappy, Calm, Stressed, Motivated, Tired"
        )
        if mood:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("journal_entries.txt", "a") as file:
                file.write(f"{timestamp}\n")
                file.write(f"Journal: {entry}\n")
                file.write(f"Mood: {mood}\n\n")

#Affirmations
def get_random_affirmation():
    affirmations = [
        "I am growing stronger every day.",
        "I am calm, capable, and resilient.",
        "Every step I take is progress.",
        "I choose peace over worry.",
        "I am proud of how far I've come."
    ]
    return random.choice(affirmations)

#Affirmation format
def fade_in_affirmation(affirmation):
    affirmation_label.config(text=affirmation)

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

#Long break
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)

        pose_img, pose_filename = get_random_pose_image()
        pose_image_label.config(image=pose_img)
        pose_image_label.image = pose_img

        caption_text = pose_filename.replace('_', ' ').replace('.png', '').replace('.jpg', '').title()
        pose_caption_label.config(text=caption_text)

        reminder = random.choice(reminder_messages)
        check_mark.config(text=reminder)

        play_soft_sound()
        change_background_color(window, "#ffe0b2")

        affirmation_label.config(text="")

#Short break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)

        pose_img, pose_filename = get_random_pose_image()
        pose_image_label.config(image=pose_img)
        pose_image_label.image = pose_img

        caption_text = pose_filename.replace('_', ' ').replace('.png', '').replace('.jpg', '').title()
        pose_caption_label.config(text=caption_text)

        reminder = random.choice(reminder_messages)
        check_mark.config(text=reminder)

        play_soft_sound()
        change_background_color(window, "#e0f7fa")

        affirmation_label.config(text="")
        
#Work affirmation
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

        change_background_color(window, "#ffffff")

        affirmation = get_random_affirmation()
        affirmation_label.config(text="")
        fade_in_affirmation(affirmation)

        pose_image_label.config(image="")
        pose_caption_label.config(text="")

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()

        if reps % 2 == 1:
            prompt_journal_entry()

        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks)

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    affirmation_label.config(text="")
    pose_image_label.config(image="")
    pose_caption_label.config(text="")
    global reps
    reps = 0
    change_background_color(window, YELLOW)

def play_soft_sound():
    pass  # Implement soft sound if needed

def change_background_color(win, color):
    win.config(bg=color)
    canvas.config(bg=color)
    check_mark.config(bg=color)
    title_label.config(bg=color)
    affirmation_label.config(bg=color)
    pose_image_label.config(bg=color)
    pose_caption_label.config(bg=color)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("SoulCare Central")
window.config(padx=50, pady=50, bg=YELLOW)
window.geometry("600x700")  # 🔥 New: make the app window bigger

# Title label at top
title_label = Label(text="SoulCare Central", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
title_label.grid(column=1, row=0)

# BIGGER Canvas for timer
canvas = Canvas(width=400, height=450, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)

# Load and resize logo image to fit bigger canvas
original_logo = Image.open("soulcare_logo.png")
resized_logo = original_logo.resize((400, 450))  # 💥 Match new canvas size
logo = ImageTk.PhotoImage(resized_logo)

# Place logo inside canvas
canvas.create_image(200, 225, image=logo)

# Bigger Timer Text in Center
timer_text = canvas.create_text(200, 225, text="00:00", fill="white", font=(FONT_NAME, 48, "bold"))

# Start Button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Checkmark Label (completed sessions)
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

# Affirmation label
affirmation_label = Label(text="", font=(FONT_NAME, 14, "italic"), fg="black", bg=YELLOW)
affirmation_label.grid(column=1, row=4)

# Stretch Pose image (optional)
pose_image_label = Label(window, bg=YELLOW)
pose_image_label.grid(column=1, row=5)

# Stretch Pose caption
pose_caption_label = Label(window, text="", font=(FONT_NAME, 12), bg=YELLOW)
pose_caption_label.grid(column=1, row=6)

# Start the app
window.mainloop()
