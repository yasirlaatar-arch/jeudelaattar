import tkinter as tk
from tkinter import messagebox

# الصوت (Windows)
try:
    import winsound
    def play_sound(type):
        if type == "win":
            winsound.Beep(800, 300)
        elif type == "draw":
            winsound.Beep(400, 300)
except:
    def play_sound(type):
        pass

# إعدادات النافذة
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# المتغيرات
current_player = "X"
buttons = [""] * 9
score = {"X": 0, "O": 0}

# الألوان
colors = {
    "X": "#00bfff",  # أزرق
    "O": "#ff4d4d"   # أحمر
}

# التحقق من الفائز
def check_winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in wins:
        if buttons[a] == buttons[b] == buttons[c] != "":
            return buttons[a]

    if "" not in buttons:
        return "Draw"

    return None

# تحديث السكور
def update_score():
    score_label.config(
        text=f"Player X: {score['X']}     Player O: {score['O']}"
    )

# عند الضغط على زر
def on_click(index):
    global current_player

    if buttons[index] == "":
        buttons[index] = current_player
        btns[index].config(
            text=current_player,
            fg=colors[current_player]
        )

        winner = check_winner()
        if winner:
            if winner == "Draw":
                play_sound("draw")
                messagebox.showinfo("Result", "🤝 تعادل!")
            else:
                play_sound("win")
                score[winner] += 1
                update_score()
                messagebox.showinfo("Result", f"🎉 اللاعب {winner} فاز!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

# إعادة تعيين اللوحة فقط
def reset_board():
    global current_player, buttons
    current_player = "X"
    buttons = [""] * 9
    for btn in btns:
        btn.config(text="", fg="white")

# إعادة كلشي
def reset_all():
    score["X"] = 0
    score["O"] = 0
    update_score()
    reset_board()

# العنوان
title = tk.Label(
    root,
    text="Tic Tac Toe",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=10)

# السكور
score_label = tk.Label(
    root,
    text="Player X: 0     Player O: 0",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e1e"
)
score_label.pack(pady=5)

# إطار اللعبة
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

btns = []

for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 24, "bold"),
        width=4,
        height=2,
        bg="#2d2d2d",
        fg="white",
        activebackground="#3e3e3e",
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    btns.append(btn)

# أزرار التحكم
control_frame = tk.Frame(root, bg="#1e1e1e")
control_frame.pack(pady=15)

reset_btn = tk.Button(
    control_frame,
    text="🔄 Restart Round",
    font=("Arial", 11),
    bg="#444",
    fg="white",
    command=reset_board
)
reset_btn.grid(row=0, column=0, padx=5)

reset_all_btn = tk.Button(
    control_frame,
    text="🗑️ Reset Score",
    font=("Arial", 11),
    bg="#444",
    fg="white",
    command=reset_all
)
reset_all_btn.grid(row=0, column=1, padx=5)

root.mainloop()
