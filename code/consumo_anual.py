"""
Formatar dados de consumo anual da EPE.

Uso:
    python consumo_anual.py \
            ../data/EPE/consumo_anual_energia_por_classe_1995-2018.xls \
            ../data/EPE/consumo_anual_energia_por_classe_1995-2018.csv
"""
import sys
import pandas as pd


def main():

    # Carregar dados
    df = pd.read_excel(sys.argv[1], skiprows=4)

    # Obter dados de consumo
    consumos_idx = df[df["Unnamed: 0"] == "CONSUMO (GWh)"].index
    consumos_idx = [range(i, i+6) for i in consumos_idx]
    consumos_idx = [item for sublist in consumos_idx for item in sublist]

    # Obter e formatar anos
    anos = df[df["Unnamed: 0"] == "CONSUMO (GWh)"].iloc[:, 1:].values
    anos = [str(item)[:4] for sublist in anos for item in sublist]

    # Concatenar tabelas de consumo
    df = df.iloc[consumos_idx, :]
    df = df[df["Unnamed: 0"] != "CONSUMO (GWh)"].reset_index(drop=True)
    df = df.set_index("Unnamed: 0")
    df = pd.concat((df.iloc[:5, :], df.iloc[5:10, :], df.iloc[10:, :]), axis=1)

    # Formatação final
    df.columns = anos
    df = df.T.dropna()
    df.index.name = "ANO"

    # Exportar
    df.to_csv(sys.argv[2])


if __name__ == "__main__":
    main()