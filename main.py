import tkinter
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", bg = YELLOW, fg = GREEN, font=(FONT_NAME, 35, "normal"))
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0
    progress_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Break", bg = YELLOW, fg = RED, font=(FONT_NAME, 35, "normal"))
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        timer_label.config(text="Break", bg = YELLOW, fg = PINK, font=(FONT_NAME, 35, "normal"))
        count_down(SHORT_BREAK_MIN*60)
    else:
        timer_label.config(text="Work", bg = YELLOW, fg = GREEN, font=(FONT_NAME, 35, "normal"))
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        progress_label.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 12), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 12), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

progress_label = tkinter.Label(text="", font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
progress_label.grid(column=1, row=3)

window.mainloop()