import random
import tkinter as tk
import pygame

# Stretch / Water Reminders
reminder_poses = [
    "🧘 Time to stretch your arms and legs!",
    "💧 Drink a glass of water!",
    "🌬️ Take 3 deep breaths.",
    "🚶‍♀️ Walk around for a minute.",
    "📴 Close your eyes, unclench your jaw, and relax your shoulders."
]

# Play a soft sound
def play_soft_sound():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("soft_chime.wav")
        pygame.mixer.music.play()
    except Exception as e:
        print("Could not play sound:", e)

# Change background color
def change_background_color(window, color):
    try:
        window.configure(bg=color)
    except:
        print("Could not change background color.")
