import os
import pandas as pd

FOLDER_OUTPUT = "data/output/"


def read_input():
    """Reads a simple Excel-file containing two columns.
       Column1 contains random values A, B, or C.
       Column2 contains random integers between 1 and 100.
    """
    df = pd.read_excel("data/input/input.xlsx")

    return df


def split_dataframe(df, col):
    """We split the dataframe according to the content
    in column 'col'. We return a list of tuples containing the
    value of the column and the corresponding dataframe.
    """
    values_col = df[col].unique()

    dfs = [
        (v, df[df[col] == v].reset_index(drop=True))
        for v in values_col
    ]

    return dfs


def export(dfs):
    """We export all the files to the output-folder."""
    for v, df in dfs:
        name_export = f"{v}.xlsx"
        df.to_excel(os.path.join(FOLDER_OUTPUT, name_export), index=False)


def main():
    # Read the input-file
    df_input = read_input()

    # Generate separate dataframes according to the content in "Column1"
    dfs_split = split_dataframe(df_input, "Column1")

    # Export the dataframes to the output folder
    export(dfs_split)


if __name__ == "__main__":
    main()
