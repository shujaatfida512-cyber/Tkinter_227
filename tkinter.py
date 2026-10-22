import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Study program Prediction")
root. geometry("600x600")

judul = tk.Label(
    root,
    text = "Study program Prediction",
    font = ("Arial", 16, "bold")
)

judul.pack(pady=20)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

