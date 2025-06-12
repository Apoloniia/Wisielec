# 🧪 Raport z Testów Gry "Wisielec"

**Data testu:** 12.06.2025  
**Wersja testowana:** v0.1.1  
**Osoba testująca:** Agata Wójcik  
**Typ testów:** Manualne  
**Środowisko testowe:**  
- **System operacyjny:** Windows 11  
- **Przeglądarka / platforma:** desktop  

---

## 1. 🎯 Cele testu
- Sprawdzenie poprawności działania podstawowych funkcjonalności gry.  
- Weryfikacja zgodności interfejsu z założeniami projektu.  
- Wykrycie błędów wpływających na rozgrywkę i użytkownika.  
- Ocena wydajności i responsywności gry.  

---

## 2. 📌 Zakres testów
- Uruchomienie gry i załadowanie interfejsu głównego  
- Wprowadzenie poprawnych i niepoprawnych liter  
- Obsługa błędnych danych wejściowych (np. cyfry, znaki specjalne)  
- Obsługa wygranej i przegranej  

---

## 3. ✅ Wyniki testów

| ID   | Scenariusz testowy                            | Oczekiwany rezultat                                                       | Rzeczywisty rezultat                                                                 | Status      | Uwagi / Błąd   |
|------|-----------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-------------|----------------|
| T01  | Uruchomienie gry                              | Gra się ładuje bez błędów                                                 | Gra się uruchamia poprawnie                                                           | ✅ Pass     | -              |
| T02  | Wprowadzenie poprawnej litery                 | Litera zostaje odkryta w słowie                                           | Działa zgodnie z oczekiwaniami                                                        | ✅ Pass     | -              |
| T03  | Wprowadzenie niepoprawnej litery              | Litera nie zostaje odkryta, rysuje się kolejny element wisielca          | Działa zgodnie z oczekiwaniami                                                        | ✅ Pass     | -              |
| T04  | Wprowadzenie cyfry/znaku specjalnego          | Gra odrzuca dane                                                          | Działa zgodnie z oczekiwaniami                                                        | ✅ Pass     | -              |
| T05  | Wprowadzenie litery specjalnej                | Gra odrzuca dane                                                          | Wczytuje normalnie                                                                    | ❌ Fail     | BUG-001        |
| T06  | Odgadnięcie hasła przed końcem gry            | Komunikat o wygranej                                                      | Pojawia się okno dialogowe, potem drugie z tym samym komunikatem                     | ⚠️ Partial  | Do poprawy     |
| T07  | Nieodgadnięcie hasła przed końcem gry         | Komunikat o przegranej                                                    | Pojawia się okno dialogowe, potem drugie z tym samym komunikatem                     | ⚠️ Partial  | Do poprawy     |
| T08  | Otwarcie rankingu                             | Wyświetlenie top 5 oraz historii gier                                     | Działa zgodnie z oczekiwaniami                                                        | ✅ Pass     | -              |
| T09  | Wyjście z gry                                 | Aplikacja się zamyka                                                      | Działa zgodnie z oczekiwaniami                                                        | ✅ Pass     | -              |

---

## 4. 🐞 Błędy zidentyfikowane podczas testów

| ID błędu | Opis                                   | Krok reprodukcji                              | Priorytet | Status     | Zgłoszono do  |
|----------|----------------------------------------|-----------------------------------------------|-----------|------------|---------------|
| BUG-001  | Aplikacja wczytuje litery specjalne     | Uruchom grę → wpisz np. „é” → kliknij OK       | Wysoki    | Zgłoszony  | Development   |

---

## 5. 📝 Podsumowanie i rekomendacje

**Ogólna stabilność:** Zadowalająca, lecz wymaga poprawy walidacji danych wejściowych.

### ✅ Rekomendacje:
- Dodać **walidację wejścia**, aby akceptowane były tylko litery alfabetu łacińskiego.
- Usprawnić **mechanizm resetowania gry** i obsługi komunikatów końcowych.
- Rozważyć dodanie **testów automatycznych** dla podstawowych przypadków użycia.
