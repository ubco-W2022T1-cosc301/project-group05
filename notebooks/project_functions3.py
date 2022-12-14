import pandas as pd


def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)
   
    # dropping col
    drop_col = ['traveltime','failures', 'nursery','guardian', 'Medu', 'Fedu', 'reason', 'schoolsup', 'famsup', 'paid','Fjob','Mjob', 'famrel', 'famsize', 'Pstatus'
        ,'higher', 'romantic', 'internet', 'address', 'activities']
    # renaming col
    ren = {'Walc': 'Weekend_Alc_Consumption', 'Dalc': 'Daily_Alc_Consumption', 'freetime': 'Freetime', 'goout': 'Go_Out',
    'age': 'Age', 'school':'School', 'sex': 'Sex', 'health': 'Health', 'absences': 'Absences', 'G1': 'Period_1_Grade', 
    'G2': 'Period_2_Grade', 'G3': 'Final_Grade', 'studytime': 'Study_Time'}
    # col to be sorted
    sort = ['Weekend_Alc_Consumption','Daily_Alc_Consumption','Freetime', 'Final_Grade']
    # rephrase value of col
    rep = {'F': 'Female', 'M': 'Male', 'GP': 'Gabriel Pereira', 'MS': 'Mousinho Da Silveira'}

    df1 = (   
    pd.read_csv(url_or_path_to_csv_file, engine='python', on_bad_lines='skip')
        .rename(columns=ren)
        .replace(rep)
        .drop(drop_col, axis=1)
        .sort_values(sort, ascending=False)
    )

    cleaned_data = (
        df1
        .assign(Weekly_Drinking_AVG=df1['Weekend_Alc_Consumption']+df1['Daily_Alc_Consumption']/2)
        .assign(Use_Of_Freetime=df1['Freetime']+df1['Study_Time']+df1['Go_Out']/3)
    )

    return cleaned_data

# Sourced it from Ben's project_Functions2. Thought it was a super useful function.
def combine_subj(subject_dict):
   
    for key, val in subject_dict.items():
        val['subject'] = key
    
    p_dfs = [val for key, val in subject_dict.items()]

    return pd.concat(p_dfs, ignore_index=True)

