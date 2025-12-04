# gui_widgets.py
# Reusable GUI widgets and styling

import tkinter as tk
from config import BUTTON_BG, BUTTON_HOVER


def style_button(button):
    """Apply standard button styling"""
    button.config(
        bg=BUTTON_BG,
        fg="white",
        bd=0,
        padx=12,
        pady=6,
        font=("Segoe UI", 11, "bold"),
        activebackground=BUTTON_HOVER
    )
    button.bind("<Enter>", lambda e: button.config(bg=BUTTON_HOVER))
    button.bind("<Leave>", lambda e: button.config(bg=BUTTON_BG))


def create_styled_button(parent, text, command, bg=BUTTON_BG, hover=BUTTON_HOVER):
    """Create a pre-styled button"""
    button = tk.Button(
        parent,
        text=text,
        command=command,
        bg=bg,
        fg="white",
        bd=0,
        padx=12,
        pady=6,
        font=("Segoe UI", 11, "bold"),
        activebackground=hover
    )
    button.bind("<Enter>", lambda e: button.config(bg=hover))
    button.bind("<Leave>", lambda e: button.config(bg=bg))
    return button


def create_label_entry_pair(parent, label_text, row, entry_width=25):
    """Create a label-entry pair in RTL layout"""
    label = tk.Label(parent, text=label_text, bg="white")
    label.grid(row=row, column=1, sticky="e", padx=5)
    
    entry = tk.Entry(parent, width=entry_width, justify="right")
    entry.grid(row=row, column=0, sticky="ew", padx=5)
    
    return label, entry