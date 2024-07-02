import argparse
import pandas as pd
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt


def read_data_from_csv_file(filepath):
    df = pd.read_csv(filepath, delimiter=';', header=None)
    return df


def make_time_list(sampling, samples):
    span = 1 / sampling
    list = []
    counter = 0
    for i in range(samples):
        list.append(counter)
        counter += span
    return list


def prepare_input_dataframe(df, time_f: bool, sampling=0, samples=0):
    if time_f:
        time_df = pd.DataFrame(df.iloc[:, 0].values)
        eeg_data = pd.DataFrame(df.iloc[:, 1:].values)
    else:
        time_df = pd.DataFrame(make_time_list(sampling, samples))
        eeg_data = df.head(samples)

        if time_df.shape[0] != eeg_data.shape[0]:
            raise ValueError("Niepoprawna liczba próbek")

    return time_df, eeg_data


def make_oscillogram_from_data(time_df, data_df, filename, flag):
    if flag == "input":
        title = "Oscylogram danych wejściowych"
        lbl = "Kanał "

    else:
        title = "Wyodrębnione komponenty"
        lbl = "Komponent "

    canals = data_df.shape[1]
    for i in range(canals):
        plt.plot(time_df.values, data_df.values[:, i], label=lbl + str(i + 1))
    plt.tight_layout()
    plt.legend()
    plt.title(title)
    plt.savefig(filename)
    plt.clf()


def fast_ica(eeg_data):
    components = eeg_data.shape[1]
    ica = FastICA(n_components=components, random_state=42, max_iter=1000)
    S_ = ica.fit_transform(eeg_data)  # S_ zawiera komponenty niezależne
    return pd.DataFrame(S_)


def remove_components(to_remove, components):
    return components.drop(components.columns[[r - 1 for r in to_remove]], axis=1)


def remove_time_from_df(df):
    return df.drop(df.columns[0], axis=1)


def save_cleaned_data_to_file(cleaned_data, filepath):
    cleaned_df = pd.DataFrame(cleaned_data)
    cleaned_df.to_csv(filepath, index=False, header=False, sep=';')
    print("Pomyślnie zapisano dane do pliku ", filepath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('source', metavar='PLIK_WEJSCIOWY', type=str)
    parser.add_argument('target', metavar='PLIK_WYNIKOWY', type=str)

    parser.add_argument('-d', type=str, default="data_oscillogram.png")
    parser.add_argument('-c', type=str, default="components_oscillogram.png")
    parser.add_argument('-s', type=int, default=None)
    parser.add_argument('-n', type=int, default=None)
    parser.add_argument('-t', action='store_true')

    args = parser.parse_args()

    df = read_data_from_csv_file(args.source)

    if args.t and (args.s or args.n is not None):
        df = remove_time_from_df(df)
        args.t = False

    time_df, eeg_data = prepare_input_dataframe(df, args.t, args.s, args.n)
    make_oscillogram_from_data(time_df, eeg_data, args.d, "input")
    components = fast_ica(eeg_data)

    make_oscillogram_from_data(time_df, components, args.c, "components")

    if str(input("Czy chcesz usunąć któryś z komponentów? [T/n]\n")) not in ["T", "t"]:
        save_cleaned_data_to_file(components, args.target)
        exit(0)

    i = input(f"Podaj oddzielone spacjami numery komponentów, (wg pliku {args.c}), który chcesz usunąć: ")

    c_to_rem = []
    for number in i.split():
        if number.isdigit():
            c_to_rem.append(int(number))
    print("Usuwanie komponentów: ", c_to_rem)
    components = remove_components(c_to_rem, components)
    save_cleaned_data_to_file(components, args.target)
    exit(0)
