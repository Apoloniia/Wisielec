from gra import load_words_from_file, choose_word
import tkinter as tk
from tkinter import messagebox

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
    slowa = load_words_from_file()
    kategoria, slowo = choose_word(slowa)
    slowo = slowo.upper()
    if not slowo:
        messagebox.showerror("Błąd", "Nie znaleziono słowa do odgadnięcia.")
        return
    odkryte = ["_" if znak.isalpha() else znak for znak in slowo]
    uzyte_litery = set()
    bledy = 0

    gra_frame = tk.Frame(root, bg="#2b2b2b")
    gra_frame.pack(expand=True, fill="both")

    # Górny pasek z kategorią i przyciskiem powrotu
    top_frame = tk.Frame(gra_frame, bg="#2b2b2b")
    top_frame.pack(fill="x", pady=10, padx=10)

    kategoria_label = tk.Label(
        top_frame,
        text=f"Kategoria: {kategoria}",
        font=("Georgia", 30),
        fg="white",
        bg="#2b2b2b"
    )
    kategoria_label.pack(side="left")

    powrot_btn = tk.Button(
        top_frame,
        text="Powrót",
        command=lambda: (gra_frame.destroy(), stworz_menu_glowne()),
        bg="#444",
        fg="white",
        activebackground="#666",
        activeforeground="white",
        font=("Georgia", 30)
    )
    powrot_btn.pack(side="right")

    # Główna część gry
    main_game_frame = tk.Frame(gra_frame, bg="#2b2b2b")
    main_game_frame.pack(expand=True)

    canvas = tk.Canvas(main_game_frame, width=300, height=400, bg="#2b2b2b", highlightthickness=0)
    canvas.grid(row=0, column=0, rowspan=4, padx=20, pady=10)

    slowo_var = tk.StringVar(value=" ".join(odkryte))
    slowo_label = tk.Label(main_game_frame, textvariable=slowo_var, font=("Georgia", 32), fg="white", bg="#2b2b2b")
    slowo_label.grid(row=0, column=1, pady=10, sticky="n")

    litera_var = tk.StringVar()
    litera_entry = tk.Entry(main_game_frame, textvariable=litera_var, font=("Georgia", 24), width=2, justify="center")
    litera_entry.grid(row=1, column=1, pady=10)

    uzyte_var = tk.StringVar(value="Użyte litery: ")
    uzyte_label = tk.Label(main_game_frame, textvariable=uzyte_var, font=("Georgia", 16), fg="white", bg="#2b2b2b")
    uzyte_label.grid(row=2, column=1, pady=10)

    def rysuj_wisielca():
        canvas.delete("all")
        canvas.create_line(50, 350, 250, 350, fill="white", width=5)
        canvas.create_line(150, 350, 150, 50, fill="white", width=5)
        canvas.create_line(150, 50, 220, 50, fill="white", width=5)
        canvas.create_line(220, 50, 220, 80, fill="white", width=5)
        if bledy >= 1: canvas.create_oval(200, 80, 240, 120, fill="white")
        if bledy >= 2: canvas.create_line(220, 120, 220, 200, fill="white", width=4)
        if bledy >= 3: canvas.create_line(220, 140, 190, 170, fill="white", width=4)
        if bledy >= 4: canvas.create_line(220, 140, 250, 170, fill="white", width=4)
        if bledy >= 5: canvas.create_line(220, 200, 190, 250, fill="white", width=4)
        if bledy >= 6: canvas.create_line(220, 200, 250, 250, fill="white", width=4)
        if bledy >= 7:
            canvas.create_text(150, 20, text="YOU ARE FAILURE", fill="red", font=("Georgia", 24, "bold"))

    def sprawdz_litere(event=None):
        nonlocal bledy
        lit = litera_var.get().upper()
        litera_var.set("")
        if not lit.isalpha() or len(lit) != 1 or lit in uzyte_litery:
            return
        uzyte_litery.add(lit)
        uzyte_var.set("Użyte litery: " + ", ".join(sorted(uzyte_litery)))
        if lit in slowo:
            for i, znak in enumerate(slowo):
                if znak == lit:
                    odkryte[i] = lit
            slowo_var.set(" ".join(odkryte))
        else:
            bledy += 1
        rysuj_wisielca()

        def pokaz_wynik(tekst):
            gra_frame.destroy()
            wynik_frame = tk.Frame(root, bg="#2b2b2b")
            wynik_frame.pack(expand=True, fill="both")

            wynik_label = tk.Label(wynik_frame, text=tekst, font=("Georgia", 28, "bold"), fg="white", bg="#2b2b2b")
            wynik_label.pack(pady=40)

            powrot_btn = tk.Button(
                wynik_frame,
                text="Powrót do Menu Głównego",
                font=("Georgia", 18, "bold"),
                bg="#444",
                fg="white",
                activebackground="#666",
                activeforeground="white",
                command=lambda: (wynik_frame.destroy(), stworz_menu_glowne())
            )
            powrot_btn.pack(pady=20)

        if "_" not in odkryte:
            pokaz_wynik(f"Triumf! Odgadłeś/aś: {slowo}")
        elif bledy >= MAKS_BLEDOW:
            pokaz_wynik(f"Zgon... Słowo brzmiało: {slowo}")

    litera_entry.bind("<Return>", sprawdz_litere)
    litera_entry.focus()
    rysuj_wisielca()



def stworz_menu_glowne():
    global centralna_rama
    centralna_rama = tk.Frame(root, bg="#2b2b2b")
    centralna_rama.place(relx=0.5, rely=0.5, anchor="center")

    tk.Button(centralna_rama, text="Nowa Gra", font=font_style, width=20, command=nowa_gra).pack(pady=20)
    tk.Button(centralna_rama, text="Ranking", font=font_style, width=20, command=ranking).pack(pady=20)
    tk.Button(centralna_rama, text="Wyjście", font=font_style, width=20, command=wyjscie).pack(pady=20)

stworz_menu_glowne()

root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))
root.mainloop()