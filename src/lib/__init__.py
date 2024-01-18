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