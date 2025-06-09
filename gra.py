import random

#--Import  slowa wraz z kategoria--
def load_words_from_file():
    words_with_categories = []
    current_category = None

    with open("lista_slow_ascii.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.endswith(":"):
                current_category = line[:-1].strip()
            elif current_category and line.startswith("- "):
                word = line[2:].strip().lower()
                words_with_categories.append((current_category, word))

    return words_with_categories



