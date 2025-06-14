from gra import load_words_from_file, choose_word
from zapis_gier import add_game_results, load_file
from time import time
import tkinter as tk
from tkinter import messagebox
import os

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

def zasady_gry():
    global centralna_rama
    if centralna_rama is not None:
        centralna_rama.destroy()

    centralna_rama = tk.Frame(root, bg="#1e1e1e")
    centralna_rama.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

    powrot_btn = tk.Button(
        centralna_rama,
        text="Powrót do Menu Głównego",
        font=("Georgia", 18, "bold"),
        bg="#444",
        fg="white",
        activebackground="#666",
        activeforeground="white",
        command=lambda: (centralna_rama.destroy(), stworz_menu_glowne())
    )
    powrot_btn.pack(pady=(10, 30), anchor="n")

    tk.Label(
        centralna_rama,
        text="Zasady gry",
        font=("Arial", 24, "bold"),
        fg="white",
        bg="#1e1e1e"
    ).pack(pady=10)

    opis = """
    Gra w wisielca polega na odgadnięciu wylosowanego słowa z danej kategorii
    litera po literze. Gracz ma 7 prób, a jeśli nie odgadnie – przegrywa.
    """

    tk.Label(
        centralna_rama,
        text=opis,
        font=("Arial", 20),
        fg="white",
        bg="#1e1e1e",
        justify="left",
        wraplength=1000
    ).pack(pady=10)


def ranking():
    global centralna_rama

    if centralna_rama is None:
        centralna_rama = tk.Frame(root, bg="#1e1e1e")
        centralna_rama.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)
    else:
        for widget in centralna_rama.winfo_children():
            widget.destroy()
        centralna_rama.configure(bg="#1e1e1e")
        
    def wyczysc_historie():

        if messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz usunąć całą historię gier?"):
            os.remove("zapis_gier.json")
            messagebox.showinfo("Sukces", "Historia zostala wyczyszczona.")
            centralna_rama.destroy()
            stworz_menu_glowne() # Powrot do menu glownego

    history = load_file()
    game_stats = history.get("game_stats", [])

    font_title = ("Georgia", 20, "bold")
    font_text = ("Georgia", 14)


    tk.Button(
        centralna_rama, text="↩ Powrót do menu", font=("Georgia", 14),
        command=stworz_menu_glowne
    ).pack(pady=10, anchor="nw", padx=10)

    if not game_stats:
        tk.Label(
            centralna_rama, text="Brak zapisanych gier.",
            font=font_title, fg="white", bg="#1e1e1e"
        ).pack(pady=20)
        return


    tk.Button(
        centralna_rama, text="↩ Powrót do menu", font=("Georgia", 14),
        command=stworz_menu_glowne
    ).pack(pady=10, anchor="nw", padx=10)
    
    tk.Button(centralna_rama, text="🗑 Wyczyść historię", font=("Georgia", 14),
        bg="#822", fg="white",command=wyczysc_historie
        ).pack(pady=10, anchor="ne", padx=10)


    tk.Label(
        centralna_rama, text="🏆 Top 5 wygranych (najszybszych):",
        font=font_title, fg="gold", bg="#1e1e1e"
    ).pack(pady=10)

    best_games = sorted([g for g in game_stats if g["won"]], key=lambda x: x["time_taken"])[:5]
    for i, game in enumerate(best_games, 1):
        txt = f"{i}. {game['word']} - {game['time_taken']:.2f}s, Próby: {game['attempts_used']}"
        tk.Label(
            centralna_rama, text=txt, font=font_text,
            fg="white", bg="#1e1e1e"
        ).pack()

    tk.Label(
        centralna_rama, text="─" * 100, fg="gray", bg="#1e1e1e"
    ).pack(pady=10)

    tk.Label(
        centralna_rama, text="📜 Historia wszystkich gier:",
        font=font_title, fg="lightblue", bg="#1e1e1e"
    ).pack(pady=10)

    historia_frame = tk.Frame(centralna_rama, bg="#1e1e1e")
    historia_frame.pack(fill="both", expand=True, padx=20, pady=10)

    scrollbar = tk.Scrollbar(historia_frame)
    scrollbar.pack(side="right", fill="y")

    text_widget = tk.Text(
        historia_frame, font=font_text, bg="#2b2b2b", fg="white",
        yscrollcommand=scrollbar.set, wrap="word"
    )
    text_widget.pack(fill="both", expand=True)
    scrollbar.config(command=text_widget.yview)

    for g in game_stats:
        wynik = "Wygrana" if g["won"] else "Przegrana"
        line = f"{g['word']} – {wynik}, próby: {g['attempts_used']}, czas: {g['time_taken']:.2f}s\n"
        text_widget.insert("end", line)

    text_widget.config(state="disabled")


def pokaz_wynik(tekst):
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

def nowa_gra():
    global centralna_rama
    if centralna_rama is not None:
        centralna_rama.destroy()

    slowa = load_words_from_file()
    kategoria, slowo = choose_word(slowa)
    slowo = slowo.lower()
    if not slowo:
        messagebox.showerror("Błąd", "Nie znaleziono słowa do odgadnięcia.")
        return

    odkryte = ["_" if znak.isalpha() else znak for znak in slowo]
    uzyte_litery = set()
    bledy = 0
    start_time = time()

    centralna_rama = tk.Frame(root, bg="#2b2b2b")
    centralna_rama.pack(expand=True, fill="both")

    top_frame = tk.Frame(centralna_rama, bg="#2b2b2b")
    top_frame.pack(fill="x", pady=10, padx=10)

    tk.Label(top_frame, text=f"Kategoria: {kategoria}", font=("Georgia", 30), fg="white", bg="#2b2b2b").pack(side="left")

    tk.Button(
        top_frame,
        text="Powrót",
        command=lambda: (centralna_rama.destroy(), stworz_menu_glowne()),
        bg="#444",
        fg="white",
        activebackground="#666",
        activeforeground="white",
        font=("Georgia", 30)
    ).pack(side="right")

    main_game_frame = tk.Frame(centralna_rama, bg="#2b2b2b")
    main_game_frame.pack(expand=True)

    canvas = tk.Canvas(main_game_frame, width=300, height=400, bg="#2b2b2b", highlightthickness=0)
    canvas.grid(row=0, column=0, rowspan=4, padx=20, pady=10)

    slowo_var = tk.StringVar(value=" ".join(odkryte))
    tk.Label(main_game_frame, textvariable=slowo_var, font=("Georgia", 32), fg="white", bg="#2b2b2b").grid(row=0, column=1, pady=10, sticky="n")

    litera_var = tk.StringVar()
    litera_entry = tk.Entry(main_game_frame, textvariable=litera_var, font=("Georgia", 24), width=2, justify="center")
    litera_entry.grid(row=1, column=1, pady=10)

    uzyte_var = tk.StringVar(value="Użyte litery: ")
    tk.Label(main_game_frame, textvariable=uzyte_var, font=("Georgia", 16), fg="white", bg="#2b2b2b").grid(row=2, column=1, pady=10)

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
        lit = litera_var.get().lower()
        litera_var.set("")

        if len(lit) != 1 or lit in uzyte_litery or not lit.isalpha():
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

        if "_" not in odkryte:
            time_taken = time() - start_time
            add_game_results(slowo, True, len(uzyte_litery), time_taken)
            centralna_rama.destroy()
            pokaz_wynik(f"Triumf! Odgadłeś/aś: {slowo}")
        elif bledy >= MAKS_BLEDOW:
            time_taken = time() - start_time
            add_game_results(slowo, False, len(uzyte_litery), time_taken)
            centralna_rama.destroy()
            pokaz_wynik(f"Zgon... Słowo brzmiało: {slowo}")

    litera_entry.bind("<Return>", sprawdz_litere)
    litera_entry.focus()
    rysuj_wisielca()


def stworz_menu_glowne():
    global centralna_rama
    if centralna_rama is not None:
        centralna_rama.destroy()  # <<-- USUWA POPRZEDNIĄ RAMKĘ

    centralna_rama = tk.Frame(root, bg="#2b2b2b")
    centralna_rama.place(relx=0.5, rely=0.5, anchor="center")

    tk.Button(centralna_rama, text="Nowa Gra", font=font_style, width=20, command=nowa_gra).pack(pady=20)
    tk.Button(centralna_rama, text="Ranking", font=font_style, width=20, command=ranking).pack(pady=20)
    tk.Button(centralna_rama, text="Zasady gry", font=font_style, width=20, command=zasady_gry).pack(pady=20)
    tk.Button(centralna_rama, text="Wyjście", font=font_style, width=20, command=wyjscie).pack(pady=20)

stworz_menu_glowne()

root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))
root.mainloop()
