## read params
## process
## return dataframe
import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    #print(config)
    data_path = config["data_source"]["s3_source"]
    #data_path1 = os.path.join("src","__init__.py")
    #data_path = '../../Mlops-task/'+data_path
    #data_path = '../'+data_path
    #data_path = 'data_given/Admission_Prediction.csv'
    #data_path= r'C:\Users\VIMALA P T\OneDrive\Documents\Python anaconda\Ineuron\projects\MLOPS\Mlops-task\data_given\Admission_Prediction.csv'
    #data_path = r'C:\Users\VIMALA P T\OneDrive\Documents\Python anaconda\Ineuron\projects\MLOPS\Mlops-task\ + data_path'
    #data_path = os.path.join(r"C:\Users\VIMALA P T\OneDrive\Documents\Python anaconda\Ineuron\projects\MLOPS\Mlops-task",data_path)
    #data_path = data_path1 + data_path
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    return df



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default=r'C:\Users\VIMALA P T\OneDrive\Documents\Python anaconda\Ineuron\projects\MLOPS\Mlops-task\params.yaml')
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)


#with open('../../Mlops-task/params.yaml') as f:
#    data = yaml.load(f)
#    print(data)

#with open('../data_given/Admission_Prediction.csv')