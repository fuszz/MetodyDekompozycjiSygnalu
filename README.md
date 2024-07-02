# ICA tool

Projekt zaliczeniowy z przedmiotu Metody Dekompozycji Sygnału

## Zadane funkcjonalności

- Wczytanie pliku sygnału
- Wskazanie parametrów sygnału: liczby próbek i próbkowania
- Wyświetlenie sygnału jako oscylogramu
- Wykonanie analizy niezależnych składowych
- Wyświetlenie odnalezionych komponentów jako oscylogramu
- Usunięcie z sygnału wskazanego komponentu
- Zapisanie wynikowych komponentów do pliku .csv

## Uruchomienie skryptu

```
python3 ica.py PLIK_WEJŚCIOWY PLIK_WYJŚCIOWY [OPCJE]


**OPIS**

Poddaje dane dostarczone w PLIK_WEJŚCIOWY analizie niezależnych składowych (ICA)

 -t - wskazanie, że w pliku wejściowym pierwsza kolumna danych to czas. Brak oznacza brak takiej kolumny
 
 Opcjonalnie:
 -d - nazwa pliku .png z oscylogramem dostarczonych danych
 -c - nazwa pliku .png z oscylogramem komponentów wyodrębnionych w procesie ICA
 -s - próbkowanie. Domyślnie 100 Hz.
 -n - liczba próbek. Domyślnie - wszystkie podane w pliku wejściowym.

Parametry -n i -s są opcjonalne. Jeśli plik zawiera timestampy, a zostaną dostarczone argumenty -s lub -n, timestampy są ignorowane.
Jeśli plik nie zawiera timestampów, a nie zostaną podane oba -s i -n, używane są wartości domyślne

```

### Przykłady
```commandline
python3 ica.py -i dane.csv -o komponenty.csv -d oscylogram_danych.png -c oscylogram_komponentow.png -n 100
```

Poddaje analizie ICA 100 pierwszych próbek z pliku dane.csv, który nie zawiera timestampów, zatem (brak podanego -s), traktuje je 
jako odległe o 0.01 s.

```commandline
python3 ica.py -i dane.csv -o komponenty.csv -d oscylogram_danych.png -c oscylogram_komponentow.png -t -n 100
```

Jak wyżej, ale timestampy są ignorowane

```commandline
python3 ica.py -i dane.csv -o komponenty.csv -d oscylogram_danych.png -c oscylogram_komponentow.png -t
```
Wartości częstotliwości i próbkowania są czytane z zawartości pliku.
