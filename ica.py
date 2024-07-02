import pandas as pd
import numpy as np
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt

def read_data_from_csv_file(filepath):
    df = pd.read_csv(filepath, delimiter=';', header=None)
    return df


def make_oscillogram_from_data(df, canals, filename='Input_data.png'):
    for i in range(canals):
        plt.plot(df.iloc[:, 0].values, df.iloc[:, i + 1].values,
                 label=f'Komponent {i + 1}')  # Użycie f-stringa do etykiet

    plt.tight_layout()
    plt.legend()
    plt.title("Oscylogram danych wejściowych")
    plt.savefig(filename)


def fast_ica(df, components, filename='Saved_plot.png'):
    time = df.iloc[:, 0].values
    eeg_data = df.iloc[:, 1:].values

    ica = FastICA(n_components=components, random_state=42, max_iter=1000)
    S_ = ica.fit_transform(eeg_data)  # S_ zawiera komponenty niezależne
    A_ = ica.mixing_  # A_ to macierz miksująca

    plt.figure(figsize=(12, 6))
    for i in range(components):
        plt.subplot(components, 1, i + 1)
        plt.plot(time, S_[:, i])
        plt.title(f'Komponent {i + 1}')
        plt.xlabel('Czas (s)')
        plt.ylabel('Amplituda')

    plt.tight_layout()
    plt.savefig(filename)

    return S_, A_

def remove_components(artefact_components, S_):
    for i in artefact_components:
        S_ = np.delete(S_, i, axis=1)
    return S_


def save_cleaned_data_to_file(cleaned_data, filepath):
    cleaned_df = pd.DataFrame(cleaned_data)
    cleaned_df.to_csv(filepath, index=False, sep=';')



df = read_data_from_csv_file("./Dane/eeg_czas_2_128_129.csv")
make_oscillogram_from_data(df, 2)
S_, A_ = fast_ica(df, 2)
cleaned_data = remove_components([0], S_)
save_cleaned_data_to_file(cleaned_data, "cleaned_data.csv")