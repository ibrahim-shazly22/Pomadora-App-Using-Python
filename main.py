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
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_the_timer():
    window.after_cancel(timer)
    timer_word_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_the_timer():
    global reps
    reps+=1
    work_in_sec=WORK_MIN*60
    short_break_in_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_break_sec)
        timer_word_label.config(text="Break",fg=RED,font=(FONT_NAME,40,"bold"),bg=YELLOW)
    elif reps%2==0:
        count_down(short_break_in_sec)
        timer_word_label.config(text="Break", fg=PINK, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
    else:
        count_down(work_in_sec)
        timer_word_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
        mark=""
        for _ in range (math.floor(reps/2)):
            mark+="✔"
        check_mark_label.config(text=mark,fg=GREEN,font=(FONT_NAME,20,"bold"),bg=YELLOW)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_at_min=math.floor(count/60)
    count_at_sec=count%60
    if count_at_sec< 10:
        count_at_sec=f"0{count_at_sec}"
    if count_at_sec==0:
        count_at_sec="00"
    canvas.itemconfig(timer_text,text=f"{count_at_min}:{count_at_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count -1)  #main point in making timer
    else:
        start_the_timer()
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomadoro App")
window.config(padx=100,pady=50,bg=YELLOW)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35 , "bold"))
canvas.grid(column=1,row=1)



timer_word_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,40,"bold"),bg=YELLOW)
timer_word_label.grid(column=1,row=0)



start_button=Button(text="Start",font=(FONT_NAME,10,"bold"),command=start_the_timer)
start_button.grid(column=0,row=2)


reset_button=Button(text="Reset",font=(FONT_NAME,10,"bold"),command=reset_the_timer)
reset_button.grid(column=2,row=2)

check_mark_label=Label(fg=GREEN,font=(FONT_NAME,20,"bold"),bg=YELLOW)
check_mark_label.grid(column=1,row=3)











window.mainloop()
