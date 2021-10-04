#!/usr/bin/env python
"""
Formatar dados de balanço dos centros de transformação da EPE.

Uso:
    python balanco_centros_transformacao.py \
            ../data/EPE/balanco_centros_transformacao.xlsx \
            ../data/EPE/balanco_centros_transformacao.csv
"""
import sys
import pandas as pd


def main():

    # Dicionário de tabelas. Primeiro valor é skiprows, segundo é nrows.
    tables = {
        "PETRÓLEO": (2, 14),
        "GÁS NATURAL": (25, 8),
        "CENTRAIS ELÉTRICAS": (39, 42),
    }
    # Dicionário de DataFrames
    dfs = {}

    # Iterar tabelas
    for k, v in tables.items():
        # Carregar dados
        df_ = pd.read_excel(
            sys.argv[1],
            skiprows=v[0],
            nrows=v[1],
        )

        # Formatar dados
        df_ = df_.iloc[:, :52]
        df_.iloc[:, 0] = df_.iloc[:, 0].str.strip()
        df_.insert(1, "CATEGORIA", k)
        df_ = df_.rename(
            columns={df_.columns[0]: "FONTES", df_.columns[1]: "IDENTIFICAÇÃO"}
        )
        df_["FONTES"] = df_["FONTES"].replace("FONTES", "FONTES " + k)

        # Adicionar DataFrame ao dicionário
        dfs[k] = df_

    # Concatenar DataFrames e escrever resultado.
    df = pd.concat(dfs.values(), ignore_index=True)
    df.to_csv(sys.argv[2], index=False)


if __name__ == "__main__":
    main()
