import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, marks, timer
    # only cancel if a timer exists
    if timer is not None:
        window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    checks.config(text="", fg=GREEN, bg=YELLOW)
    start_button.config(state="normal")
    reps = 0
    marks = ""
    timer = None

# ---------------------------- CHECK FUNCTION ------------------------------- #

def check_marks():
    global reps, marks
    # build marks fresh (avoid accidental duplicates) and update UI
    check_mark_count = reps // 2
    marks = "✓" * check_mark_count
    checks.config(text=marks)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    start_button.config(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <= 9:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        check_marks()
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# ensure the image file path is relative to the script
tomato_img = tk.PhotoImage(file="tomato.png") # Create image
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) # Create text
canvas.grid(column=1, row=1)

# Other UI elements
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 42), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = tk.Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

checks = tk.Label(bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
checks.grid(column=1, row=3)

# Main Loop
window.mainloop()

