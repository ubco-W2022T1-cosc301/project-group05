import pandas as pd


def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)
   
    drop_col = ['traveltime','failures', 'nursery','guardian', 'Medu', 'Fedu', 'reason', 'schoolsup', 'famsup', 'paid','Fjob','Mjob', 'famrel', 'famsize', 'Pstatus'
        ,'higher', 'romantic', 'internet', 'address', 'activities']
    ren = {'Walc': 'Weekend_Alc_Consumption', 'Dalc': 'Daily_Alc_Consumption', 'freetime': 'Freetime', 'goout': 'Go_Out',
    'age': 'Age', 'school':'School', 'sex': 'Sex', 'health': 'Health', 'absences': 'Absences', 'G1': 'Period_1_Grade', 
    'G2': 'Period_2_Grade', 'G3': 'Final_Grade', 'studytime': 'Study_Time'}
    sort = ['Weekend_Alc_Consumption','Daily_Alc_Consumption','Freetime', 'Final_Grade']
    rep = {'F': 'Female', 'M': 'Male', 'GP': 'Gabriel Pereira', 'MS': 'Mousinho Da Silveira'}

    df1 = (   
    pd.read_csv(url_or_path_to_csv_file, engine='python', on_bad_lines='skip')
        .rename(columns=ren)
        .replace(rep)
        .drop(drop_col, axis=1)
        .sort_values(sort, ascending=False)
    )

    df2 = (
        df1
        .assign(df1.mean(Weekly_Drinking_AVG=df1['Weekend_Alc_Consumption']+df1['Daily_Alc_Consumption']/2))
        

    )

    return df2

