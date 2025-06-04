import json
from datetime import datetime
import os
history_file="zapis_gier.json"
def load_file():
    #Otwiera plik z historią lub tworzy pustą liste, w przypadku jego braku
    if not os.path.exists(history_file):
        return {"number_of_games": 0, "number_of_wins": 0, "number_of_losses": 0, "game_stats": []}
    with open(history_file, "r", encoding="utf-8") as file:
        return json.load(file)


def save_history(data):
    with open(history_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def add_game_results(word, won, attempts_used, time_taken_sec):
    history=load_file()
    history["number_of_games"] +=1
    if won: #zmienna boolowska określająca czy była wygrana
    history["number_of_wins"]+=1
    else: history["number_of_losses"] +=1

    game_record = {
        "timestamp": datetime.now().isoformat(),  # aktualna data i godzina w formacie ISO
        "word": word,
        "won": won,
        "attempts_used": attempts_used,
        "time_taken": round(time_taken_sec, 2)
    }
    history["game_stats"].append(game_record)
    save_history(history)
