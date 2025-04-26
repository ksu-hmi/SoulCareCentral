from tkinter import *
import math
import time
from reminder_messages 
import reminder_messages, play_soft_sound, change_background_color
import random
from reminder_messages import reminder_messages, play_soft_sound, change_background_color, get_random_affirmation
import random
from affirmations import get_random_affirmation

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 60
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
reps = 0
timer = None
# TIMER RESET

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# TIMER MECHANISM
def start_timer():
    global reps
    reps = reps+1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=GREEN)

        reminder = random.choice(reminder_messages)
        check_mark.config(text=reminder)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

        reminder = random.choice(reminder_messages)
        check_mark.config(text=reminder)

    else:
    count_down(work_sec)
    title_label.config(text="Work", fg=RED)
    change_background_color(window, "#ffffff")  # White background

    # Show a random affirmation for study time
    affirmation = get_random_affirmation()
    affirmation_label.config(text=affirmation)

    # OPTIONAL: Hide the stretch pose during work
    pose_image_label.config(image="")
    pose_caption_label.config(text="")



# Code for countdown

# Reminder Messages
import random

# SoulCare reminder messages
reminder_messages = [
    "🧘 Time to stretch your arms and legs!",
    "💧 Drink a glass of water!",
    "🌬️ Take 3 deep breaths.",
    "🚶‍♀️ Walk around for a minute.",
    "📴 Close your eyes, unclench your jaw, and relax your shoulders."
]


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
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks = marks+"✓"
        check_mark.config(text=marks)

# Stretch/Water Reminder

def start_timer():
  elif reps % 8 == 0:
    # Long break
    count_down(LONG_BREAK_MIN * 60)
    title_label.config(text="Break", fg=RED)

    reminder = random.choice(reminder_messages)
    check_marks.config(text=reminder)

#Stretch Pose
reminder = random.choice(reminder_messages)
check_marks.config(text=reminder)
pose_img = get_random_pose_image()
pose_image_label.config(image=pose_img)
pose_image_label.image = pose_img

    play_soft_sound()
    change_background_color(window, "#ffe0b2")  # Light orange

  
  elif reps % 2 == 0:
     # Short break
    count_down(SHORT_BREAK_MIN * 60)
    title_label.config(text="Break", fg=PINK)

    reminder = random.choice(reminder_messages)
    check_marks.config(text=reminder)
#Stretch Pose

reminder = random.choice(reminder_messages)
check_marks.config(text=reminder)
pose_img = get_random_pose_image()
pose_image_label.config(image=pose_img)
pose_image_label.image = pose_img

    play_soft_sound()
    change_background_color(window, "#e0f7fa")  # Light teal
  
  else:
  # Change color back after breaks
    count_down(WORK_MIN * 60)
    title_label.config(text="Work", fg=GREEN)

    change_background_color(window, "#ffffff")  # White


# User Interface Code
window = Tk()
window.title("Pomodoro")   # Pomodoro Refers to tomato in italian
window.config(padx=200, pady=120, bg=GREEN)

title_label = Label(text="Pomodoro", fg=RED,bg=GREEN, font=(FONT_NAME, 20))
title_label.grid(column=1, row=0)

canvas = Canvas(width=210, height=224, bg=GREEN, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
check_mark = Label(fg=RED, bg=GREEN)
check_mark.grid(column=1, row=3)
window.mainloop()
pose_image_label = tk.Label(window, bg=YELLOW)  # Or match your background color
pose_image_label.grid(column=1, row=4)
