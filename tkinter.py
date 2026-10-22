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

entries = []

for i in range (10):
    mata_pelajaran = tk.Label(
        input_frame,
        text=f"Subject {i+1} Value:"
    )
    mata_pelajaran.grid(
        row=i, column=0, sticky="w",
        padx=10, pady=5
    )
    entry=ttk.Entry(input_frame, width=25)
    entry.grid(
            row=i, column=1, padx=10, pady=5
        )
    
    entries.append(entry)
     
def prediksi():
        hasil_label.config(
             text="Predicted Study Program: Technology"
        )
            
prediksi_button =ttk.button(
        root,
        text="Prediction Results",
        command=prediksi
    )
             
prediksi_button.pack(pady=15)
             
             
      