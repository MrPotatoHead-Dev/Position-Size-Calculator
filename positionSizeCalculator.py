import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import messagebox, StringVar
from tkinter import ttk
from tkinter import *


# changeables
bg_colour = "peach puff2"


# create window
window = tk.Tk()
window.title("Position Size Calculator")
window.geometry("500x600")
window.config(bg=bg_colour)
# create fonts
font1 = font.Font(family="helvetica", size="30")
font2 = font.Font(family="helvetica", size="10")
font3 = font.Font(family="helvetica", size="20")

# variables
answer = StringVar()
capital = StringVar()
riskk = StringVar()
pips = StringVar()
contracts = StringVar()


# function
def calculate(*args):
    try:
        acc = float(acc_size.get())
        rsk = float(risk_size.get())
        pip = float(pip_size.get())
        contracts.set(round((((acc * rsk) / pip) / 1000), 2))

    except ValueError:
        pass


# create position size label
main = tk.Label(window, text=" Position Size Calculator", bg=bg_colour, fg="blue")
main["font"] = font1
main.place(relx="0.48", rely="0.1", anchor="center")

# create account size label
size = tk.Label(window, text="Account size [$]:", bg=bg_colour)
size["font"] = font2
size.place(relx="0.25", rely="0.28")


# create size entry

acc_size = tk.Entry(window, width="10", textvariable=capital)
acc_size.place(relx="0.48", rely="0.285")

# create risk label
risk = tk.Label(window, text="Risk [%]:", bg=bg_colour)
risk["font"] = font2
risk.place(relx="0.25", rely="0.31")


# create size entry

risk_size = tk.Entry(window, width="10", textvariable=riskk)
risk_size.place(relx="0.48", rely="0.315")


# create stoploss label
risk = tk.Label(window, text="Stop loss [pips]:", bg=bg_colour)
risk["font"] = font2
risk.place(relx="0.25", rely="0.34")


# create size entry

pip_size = tk.Entry(window, width="10", textvariable=pips)
pip_size.place(relx="0.48", rely="0.345")

contracts_label = tk.Label(window, text="No. Contracts:", anchor="center")
contracts_label["font"] = font3
contracts_label.place(relx="0.25", rely="0.40")


# display the results

result_label = tk.Label(window, textvariable=contracts, bg="white", width=5)
result_label["font"] = font3
result_label.place(relx="0.62", rely="0.40")

# calculate button

button = tk.Button(
    window, text="Calculate", command=calculate, anchor="center", bg="cyan"
)
button.place(relx="0.31", rely="0.48")
button["font"] = font3

# display art
contracts_label = tk.Label(window, text="MrPotatoHead", fg="pink")
contracts_label["font"] = font2
contracts_label.place(relx="0.1", rely="0.9")

# create main loop
window.mainloop()
