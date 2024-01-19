import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

def read_raw_data():
    import pandas as pd
    """
    Summary: Read 4 files df_final_demo.txt, df_final_experiment_clients.txt, df_final_web_data_pt_1.txt and 
    df_final_web_data_pt_2.txt into separate data frames
    parameters: None
    Return: 4 Data Frame of each file, the last one being the concat of pt_1 and pt_2
    """
    df_demo = pd.read_csv(r"..\..\data_files\raw\df_final_demo.txt")
    df_exp = pd.read_csv(r"..\..\data_files\raw\df_final_experiment_clients.txt")
    df_web_1 = pd.read_csv(r"..\..\data_files\raw\df_final_web_data_pt_1.txt")
    df_web_2 = pd.read_csv(r"..\..\data_files\raw\df_final_web_data_pt_2.txt")
    df_web = pd.concat([df_web_1,df_web_2])
    return df_demo, df_exp, df_web 

def drop_na (df, threshold=0):
    """
    Summary: Given a DataFrame df, drop na values
    Parameters: DataFrame df, threshold int (optional) default is 0
    Return: Data Frame df with drop null values as specified with treshold
    """
    if  threshold==0:
        df.dropna(inplace=True)
        
    else:
        
        try:
            # drop where there is more than threshold (int) columns with null values
            df.dropna(inplace=True,thresh=threshold)
            
        except:
            print ("Error, please check optional Parameters")
            
    return df

def fill_na_mean(df,col):
    """
    Summary: Fill null values with mean of column col
    Parameters: DataFrame DF, string col (numerical column of DF)
    Return: Data frame with column col filled with mean for null values
    """
    # fill row that its missing age with mean value
    clnt_age_mean = df[col].mean()
    df[col].fillna(clnt_age_mean,inplace=True)
    return df

def split_df (df,col='Variation', comp = 'Test'):
    '''
    Summary: Applies a mask to a dataframe's column to create 2 dataframes 
    Parameters: df =  dataframe, col = column from the dataframe, comp = the comparison that you are trying to utilize in the mask.   
    Returns 2 dataframes: DataFrame with the comparison from the mask: df_1, DataFrame that is the opposite of the mask: df_2.
    '''
    mask = df[col]==comp
    df_1 = df.loc[mask]
    df_2 = df.loc[~mask]
    return df_1, df_2

def completion_rate (df):
    '''
    Summary: Creates a variable called confirm_step_count that counts the unique clients that reached that proccess step.
    Creates a variable for the amount of unique clients called total users.  
    Creates a variable that is the division between the amoun of clients that reached the confirm step and the total users.
    Parameters: df = dataframe
    Returns: completion_rate, confirm_step_count, total_users
    '''
    confirm_step_count = df[df['process_step'] == 'confirm']['client_id'].nunique()
    total_users = df['client_id'].nunique()
    completion_rate = confirm_step_count / total_users
    return completion_rate, confirm_step_count, total_users

def filter_steps(df):
    '''
    Summary: Creates masks that verify wether the process step and the previous step are correct. The previous step shouuld be 
    one step behind for the process step. The order of the process is: start,step 1, step 2, step 3 and confirm.  
    Parameters: df = dataframe
    Returns: df = dataframe
    '''
    mask_step1 = (df['process_step'] == 'step_1') & (df['previous_step'] == 'start')
    mask_step2 = (df['process_step'] == 'step_2') & (df['previous_step'] == 'step_1')
    mask_step3 = (df['process_step'] == 'step_3') & (df['previous_step'] == 'step_2')
    mask_confirm = (df['process_step'] == 'confirm') & (df['previous_step'] == 'step_3')
    df = df[mask_step1 | mask_step2 | mask_step3 | mask_confirm]
    return df
