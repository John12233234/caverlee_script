import pandas as pd
def read_txt(filepath):
    dataframe = pd.read_csv(filepath,delimiter="\t")
    dataframe.to_csv(filepath + "csv.csv",encoding='utf-8', index=False)
    return

def add_label(file):
    #first determine the number of tweets
    #for all tweets add adjacent column of labels 
    #assign labels 1 for bot 0 for human 

    

    