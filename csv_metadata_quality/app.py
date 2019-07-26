import csv_metadata_quality.fix as fix
import pandas as pd

def run():
    # Read all fields as strings so dates don't get converted from 1998 to 1998.0
    #df = pd.read_csv('/home/aorth/Downloads/2019-07-26-Bioversity-Migration.csv', dtype=str)
    #df = pd.read_csv('/tmp/quality.csv', dtype=str)
    df = pd.read_csv('/tmp/omg.csv', dtype=str)

    # Fix whitespace in all columns
    for column in df.columns.values.tolist():
        print(f'DEBUG: {column}')

        df[column] = df[column].apply(fix.whitespace)

    # Write
    df.to_csv('/tmp/omg.fixed.csv', index=False)
