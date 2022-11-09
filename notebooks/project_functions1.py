import pandas as pd

def load_and_process_data(path1, path2=None):
    """
    Loads and processes data for Student Performance analysis use.
    
    Arguments:
    path1: str 
    path for the dataset to clean
    path2: str
    optional additional path to concatenate first dataset with
    
    Returns:
    pandas dataframe
    A dataframe with all of the data that has been loaded and cleaned
    
    """
    col_remove = ["address","famsize","Pstatus","Mjob","Fjob","guardian","traveltime","failures","schoolsup","activities","nursery","internet","famrel","romantic","freetime","goout","Dalc","Walc","health","absences"]
    value_names = {'sex':{'M':'Male', 'F':'Female'},'Medu':{0:'None', 1:'Primary', 2:'Grade 5-9', 3:'Secondary', 4:'Post-Secondary'},'Fedu':{0:'None', 1:'Primary', 2:'Grade 5-9', 3:'Secondary', 4:'Post-Secondary'}, 'subject':{'M':'Math', 'P':'Portuguese'}, 'studytime':{1:'<2 hr', 2:'2-5 hr', 3:'5-10 hr', 4:'>10 hr'}, 'school':{'GP':'Gabriel Peireira', 'MS':'Mousinho da Silveira'}}

    col_names = {'paid':'extra_classes', 'Medu':'mother\'s_education', 'Fedu':'father\'s_education', 'famsup':'family_support', 'studytime':'study_time'}

    
    #Combining Data
    data1 = pd.read_csv(path1, engine='python', on_bad_lines='skip')
    data2 = pd.read_csv(path2, engine='python', on_bad_lines='skip')
    data1["subject"] = "M"
    data2["subject"] = "P"
    
    
    
    data_cleaned = (
        pd.concat([data1,data2], ignore_index=True)
        .drop(col_remove, axis=1)
        .replace(value_names)
        .rename(col_names, axis="columns")
        
        
    )
    
    data_cleaned['study_x_mother\'s_education'] = (data_cleaned['study_time']+' X '+data_cleaned['mother\'s_education'])
    data_cleaned['study_x_father\'s_education'] = (data_cleaned['study_time']+' X '+data_cleaned['father\'s_education'])
    
    
    return data_cleaned