import pandas as pd

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)
   
    
    df1 = (   
    pd.read_csv(url_or_path_to_csv_file, engine='python', on_bad_lines='skip)
    .rename(columns={"GP3": "Final Grade"})
    .assign(improved=lambda x: np.where((x.G3 > x.G1)))
    .loc[lambda x: x['Final Grade']>15]
    .sort_values("Final Grade", ascending=True)
    .reset_index(drop=True)
    .loc[:, ["Final Grade", "Walc", "improved,", "freetime"]]
    )

        
    return df1

   