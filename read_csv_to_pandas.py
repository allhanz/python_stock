import pandas as pd
import numpy as np
import os
import sys

def get_home_():
    home_path=os.getenv("HOME")
    return home_path
    
header_str=["date","open","high","low","close","volume", "_adj_close"]
ROOT_PATH="/Users/zhonghan/workspace/japan_stock_analysis/python_stock/data/stock_data/"
def read_from_csv(dir_path,datetime,stock_id,all): #specif the year
    #datatime format 20161109
    csv_data=pd.DataFrame()
    file_name_without_day=[]
    if type(stock_id) is list:
        for id in stock_id:
            file_str=str(id)+"-"+str(datetime)[:-2]
            file_name_without_day.append(file_str)
    else:
        print("stock id data error")
        exit()

    if os.path.exists(dir_path):
        file_list=list_up_files(dir_path)
        if all == True:
            for file in file_list:
                data=pd.read_csv(file)
                csv_data.append(data)
        else:
            for file_str in file_name_without_day:
                for file in file_list:
                    basename=os.path.basename(file)
                    if file_str in basename:
                        data=pd.read_csv(file)
                        csv_data.append(data)
        whole_data=set_data_header(csv_data)
        return whole_data
    else:
        print("file path does not exist!!")
        exit()


#def pandas_data_process(header,data):

def set_data_header(data):
    if type(data) is pd.core.frame.DataFrame:
        data.columns=header_str
        return data
    else:
        print("data type from csv file error!!")
        exit()

def list_up_files(file_path):
    file_list=[]
    for root, dirs, files in os.walk(file_path):
        #print(root)
        #print(dirs)
        for file in files:
            if file.endswith(".csv"):
                #print(file)
                full_path=os.path.join(root, file)
                file_list.append(full_path)
    return file_list

def main():
    dir_path=sys.argv[1]
    datetime=sys.argv[2]
    stock_id=sys.argv[3]
    read_from_csv(dir_path,datetime,stock_id)

if __name__=="__main__":
    main()
