from tkinter import *
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
timer = None
reps = 0



# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global  reps
    reps += 1
    # convert the min into seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # when 8 reps , give long break
    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    # when reps is even short break after each work timer
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    # put the work timer
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       # calls itself again and decrease the count by 1
       timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        # calculate the marks , after each set (of 2) a mark will be shown
        work_sessions = math.floor(reps/2)
        marks = ""
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# window setup
window = Tk()
window.title("Pomodoro Timer App")
window.config(padx=100, pady=50, bg=YELLOW)

# create canvas , create an image from path, creates the image on canvas with coordinates x1,y1.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# create text (at x,y location)
timer_text = canvas.create_text(100, 130, text="00:00",fill="white", font=("Arial", 35, "bold"))
canvas.grid(column=1, row=1)

# Timer text Label
title_label = Label(text="Timer", fg=GREEN,bg=YELLOW ,highlightthickness=0,font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

# checkmark Label
check_marks = Label( fg=GREEN, bg=YELLOW ,highlightthickness=0, font=(FONT_NAME, 18, "normal"))
check_marks.grid(column=1, row=3)

# start Button
start_button = Button(text="Start", width= 8,highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# reset Button
reset_button = Button(text="Reset",width=8 , highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# keep the window open
window.mainloop()