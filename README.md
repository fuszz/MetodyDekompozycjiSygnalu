# ICA tool

Projekt zaliczeniowy z przedmiotu Metody Dekompozycji Sygnału

## Funkcjonalności

- Wczytanie pliku sygnału
- Wskazanie parametrów sygnału: liczby próbek i próbkowania
- Wyświetlenie sygnału jako oscylogramu
- Wykonanie analizy niezależnych składowych
- Wyświetlenie odnalezionych komponentów jako oscylogramu
- Usunięcie z sygnału wskazanego komponentu
- Zapisanie wynikowych komponentów do pliku .csv

## Uruchomienie skryptu

```
python3 ica.py [OPCJE] PLIK_WEJŚCIOWY PLIK_WYJŚCIOWY 


Poddaje dane dostarczone w PLIK_WEJŚCIOWY analizie niezależnych składowych (ICA)

 -t - wskazanie, że w pliku wejściowym pierwsza kolumna danych to czas. Brak oznacza brak takiej kolumny
 
 Opcjonalnie:
 -d - nazwa pliku .png z oscylogramem dostarczonych danych
 -c - nazwa pliku .png z oscylogramem komponentów wyodrębnionych w procesie ICA
 -s - próbkowanie. Domyślnie 100 Hz.
 -n - liczba próbek. Domyślnie - wszystkie podane w pliku wejściowym.

Parametry -n i -s są opcjonalne. Jeśli plik zawiera timestampy, a zostaną dostarczone argumenty -s -n, timestampy są ignorowane.
Jeśli plik nie zawiera timestampów, a nie zostaną podane -s -n, używane są wartości domyślne. Do poprawnego działania wymagane są oba argumenty -s i -n, nigdy jeden z nich.
Parametr -t należy podać nawet jeśli nie chcemy brać pod uwagę timestampów z pliku, wtedy skrypt pomija pierwszą kolumnę danych.
```

### Przykłady
```commandline
python3 ica.py -d oscylogram_danych.png -c oscylogram_komponentow.png -n 100 -s 100 dane.csv komponenty.csv 
```

Plik dane.csv bez timestampów. Taktowanie 100 Hz, 100 próbek, podane nazwy plików .png oscylogramów, plik wynikowy komponenty.csv/

```commandline
python3 ica.py -t -n 100 -s 100 dane.csv komponenty.csv 
```

Plik dane.csv zawiera timestampy, ale są ignorowane (występują argumenty -s i -n). Plik celowy: komponenty.csv. Pozostawione domyślne nazwy pliku z oscylogramami

```commandline
python3 ica.py -d oscylogram_danych.png -c oscylogram_komponentow.png -t dane.csv komponenty.csv 
```
Wartości częstotliwości i próbkowania są czytane z timestampów, brak konieczności ich podawania.
