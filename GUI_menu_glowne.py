import tkinter as tk
from tkinter import messagebox
#from import pobierz_slowo
import random

# Stała
MAKS_BLEDOW = 7

# Główne okno
root = tk.Tk()
root.title("Menu Główne")
root.attributes("-fullscreen", True)
root.configure(bg="#2b2b2b")
font_style = ("Georgia", 24, "bold")

# ---------- MENU GŁÓWNE ----------
centralna_rama = tk.Frame(root, bg="#2b2b2b")
centralna_rama.place(relx=0.5, rely=0.5, anchor="center")

def wyjscie():
    root.destroy()

def ranking():
    messagebox.showinfo("Ranking", "Tu powstanie tablica")

def nowa_gra():
    centralna_rama.destroy()

    slowo, kategoria = pobierz_slowo()
    odkryte = ["_" for _ in slowo]
    uzyte_litery = []
    bledy = [0] 

    # Rysowanie
    gra_frame = tk.Frame(root, bg="#2b2b2b")
    gra_frame.pack(expand=True)

    kategoria_label = tk.Label(gra_frame, text=f"Kategoria: {kategoria}", font=("Georgia", 20, "italic"),
    fg="lightgray", bg="#2b2b2b")
    kategoria_label.grid(row=0, column=1, pady=(0, 5))

    canvas = tk.Canvas(gra_frame, width=300, height=400, bg="#2b2b2b", highlightthickness=0)
    canvas.grid(row=0, column=0, rowspan=4, padx=20)

    slowo_var = tk.StringVar(value=" ".join(odkryte))
    slowo_label = tk.Label(gra_frame, textvariable=slowo_var, font=("Georgia", 32), fg="white", bg="#2b2b2b")
    slowo_label.grid(row=1, column=1, pady=10)

    litera_var = tk.StringVar()
    litera_entry = tk.Entry(gra_frame, textvariable=litera_var, font=("Georgia", 24), width=2, justify="center")
    litera_entry.grid(row=2, column=1)

    uzyte_var = tk.StringVar(value="Użyte litery: ")
    uzyte_label = tk.Label(gra_frame, textvariable=uzyte_var, font=("Georgia", 16), fg="white", bg="#2b2b2b")
    uzyte_label.grid(row=3, column=1, pady=10)

    def rysuj_wisielca():
        canvas.delete("all")
        canvas.create_line(50, 350, 250, 350, fill="white", width=5)
        canvas.create_line(150, 350, 150, 50, fill="white", width=5)
        canvas.create_line(150, 50, 220, 50, fill="white", width=5)
        canvas.create_line(220, 50, 220, 80, fill="white", width=5)
        if bledy[0] >= 1: canvas.create_oval(200, 80, 240, 120, fill="white")
        if bledy[0] >= 2: canvas.create_line(220, 120, 220, 200, fill="white", width=4)
        if bledy[0] >= 3: canvas.create_line(220, 140, 190, 170, fill="white", width=4)
        if bledy[0] >= 4: canvas.create_line(220, 140, 250, 170, fill="white", width=4)
        if bledy[0] >= 5: canvas.create_line(220, 200, 190, 250, fill="white", width=4)
        if bledy[0] >= 6: canvas.create_line(220, 200, 250, 250, fill="white", width=4)
        if bledy[0] >= 7:
            canvas.create_text(150, 20, text="YOU ARE FAILURE", fill="red", font=("Georgia", 24, "bold"))

    def sprawdz_litere(event=None):
        lit = litera_var.get().upper()
        litera_var.set("")
        if not lit.isalpha() or len(lit) != 1 or lit in uzyte_litery:
            return
        uzyte_litery.append(lit)
        uzyte_var.set("Użyte litery: " + ", ".join(uzyte_litery))
        if lit in slowo:
            for i, znak in enumerate(slowo):
                if znak == lit:
                    odkryte[i] = lit
            slowo_var.set(" ".join(odkryte))
        else:
            bledy[0] += 1
        rysuj_wisielca()
        if "_" not in odkryte:
            messagebox.showinfo("Triumf!", f"Odgadłeś/aś: {slowo}")
            gra_frame.destroy()
        elif bledy[0] >= MAKS_BLEDOW:
            messagebox.showinfo("Zgon...", f"Słowo brzmiało: {slowo}")
            gra_frame.destroy()

    litera_entry.bind("<Return>", sprawdz_litere)
    litera_entry.focus()
    rysuj_wisielca()

# Przyciskowe trójdzielne dziedzictwo
tk.Button(centralna_rama, text="Nowa Gra", font=font_style, width=20, command=nowa_gra).pack(pady=20)
tk.Button(centralna_rama, text="Ranking", font=font_style, width=20, command=ranking).pack(pady=20)
tk.Button(centralna_rama, text="Wyjście", font=font_style, width=20, command=wyjscie).pack(pady=20)

root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))
root.mainloop()
