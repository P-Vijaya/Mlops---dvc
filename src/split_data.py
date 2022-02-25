## split the raw data
## save it in data/processed folder
import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params,get_data

def split_and_saved_data(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]
    df = pd.read_csv(raw_data_path,sep=",")
    ## to fill missing data
    df['University_Rating'] = df['University_Rating'].fillna(df['University_Rating'].mode()[0])
    df['TOEFL_Score'] = df['TOEFL_Score'].fillna(df['TOEFL_Score'].mean())
    df['GRE_Score'] = df['GRE_Score'].fillna(df['GRE_Score'].mean())
    df = df.drop('Serial_No.',axis=1)
    train,test = train_test_split(df,test_size=split_ratio,random_state=random_state)
    train.to_csv(train_data_path,sep=",",index=False,encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default=r'C:\Users\VIMALA P T\OneDrive\Documents\Python anaconda\Ineuron\projects\MLOPS\Mlops-task\params.yaml')
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)