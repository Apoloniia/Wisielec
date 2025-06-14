# 🧪 Raport z Testów Gry "Wisielec"

**Data testu:** 14.06.2025  
**Wersja testowana:** v0.2.1  
**Osoba testująca:** Agata Wójcik  
**Typ testów:** Manualne  
**Środowisko testowe:**  
- **System operacyjny:** Windows 11  
- **Przeglądarka / platforma:** desktop  

---

## 1. 🎯 Cele testu
- Sprawdzenie poprawności działania nowo dodanych funkcjonalności gry.  
- Weryfikacja zgodności interfejsu z założeniami projektu.  
- Wykrycie błędów wpływających na rozgrywkę i użytkownika.  
- Ocena wydajności i responsywności gry.  

---

## 2. 📌 Zakres testów
- Obsługa przycisku "Zasady gry"  
- Obsługa błędnych danych wejściowych  
- Obsługa wygranej i przegranej
- Obsługa okna "Ranking"

---

## 3. ✅ Wyniki testów

| ID   | Scenariusz testowy                            | Oczekiwany rezultat                                                       | Rzeczywisty rezultat                                                                 | Status      | Uwagi / Błąd   |
|------|-----------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-------------|----------------|
| T05.2  | Wprowadzenie litery specjalnej                | Gra odrzuca dane                                                          | Działa zgodnie z oczekiwaniami                                                        | ✅ Pass     | -              |
| T06.2  | Odgadnięcie hasła przed końcem gry            | Komunikat o wygranej                                                      | Działa zgodnie z oczekiwaniami                                                        | ✅ Pass     | -              |
| T07.2  | Nieodgadnięcie hasła przed końcem gry         | Komunikat o przegranej                                                    | Działa zgodnie z oczekiwaniami                                                        | ✅ Pass     | -              |
| T10  | Otwarcie pustego rankingu                     | Komunikat "Brak zapisanych gier" oraz przycisk "Powrót do menu"           | Działa zgodnie z oczekiwaniami                                                        | ✅ Pass     | -              |
| T11  | Otwarcie rankingu w celu wyczyszczenia historii| Okno rankingowe z obecnym przyciskiem "Powrót do menu" oraz "Wyczyść historię", po którego kliknięciu pojawia się zapytanie, czy użytkownik jest pewien decyzji o usunięciu całej historii; jeżeli tak, to cała historia znika | Działa zgodnie z oczekiwaniami | ✅ Pass     | -              |
| T12  | Kliknięcie przycisku "Zasady gry"           | Otwiera się okno z zapisanymi zasadami gry orazz przyciskiem "Powrót do menu" | Działa zgodnie z oczekiwaniami                                                        | ✅ Pass     | -              |

---

## 4. 🐞 Błędy zidentyfikowane podczas testów

Brak

---

## 5. 📝 Podsumowanie i rekomendacje

**Ogólna stabilność:** Zadowalająca
