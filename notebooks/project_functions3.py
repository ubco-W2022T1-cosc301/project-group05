import pandas as pd


def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)
   
    drop_col = ['guardian', 'Medu', 'Fedu', 'reason', 'schoolsup', 'famsup', 'paid',]
    ren = {'Walc': 'Weekend_Alc_Consumption', 'Dalc': 'Daily_Alc_Consumption', 'freetime': 'Freetime' }

    df1 = (   
    pd.read_csv(url_or_path_to_csv_file, engine='python', on_bad_lines='skip')
        .rename(columns=ren)
        .drop(drop_col, axis=1)
    )


    return df1


