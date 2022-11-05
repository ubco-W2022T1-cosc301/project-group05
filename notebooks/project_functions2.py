def load_and_process(url_or_path_to_csv_file):
    
    columns_to_drop = ['famsize','nursery']
    column_name_mapper = {'Pstatus': 'parent_living_status', 
          'Medu': "mother_edu", 'Fedu': 'father_edu', 'Mjob':'mother_job', 'Fjob' : 'father_job', 'reason' : 'enrollment_reason',
          'traveltime':'travel_time', 'studytime': 'weekly_study_time', 'schoolsup':'school_support', 
          'famsup': 'family_support', 'paid':'extra_paid_classes', 'activities': 'activity_participation',
          'higher': 'higher_education_plan','famrel': 'family_relations', 'freetime':'free_time', 
          'goout': 'out_w/_friends', 'Dalc' : 'weekday_alcohol', 'Walc' : 'weekend_alcohol',
          'G1': 'first_period_grade', 'G2': 'second_period_grade', 'G3':'final_grade'
         }
    
    values_to_replace = {'GP': 'Gabriel Pereira', 'MS':'Mousinho da Silveira', 'U':'urban', 'R':'rural','A': 'apart', 'T':'together'}
    
    df1 = (
    pd.read_csv(url_or_path_to_csv_file, engine='python', on_bad_lines='skip')
        .rename(columns=column_name_mapper)
        .drop(columns_to_drop, axis=1)
        .replace(values_to_replace)
    )
    
    return df1 
    
def combine_processed_subjects(subject_dict):
    
    for key, val in subject_dict.items():
        val['subject'] = key
    
    processed_dfs = [val for key, val in subject_dict.items()]
    return pd.concat(processed_dfs, ignore_index=True)