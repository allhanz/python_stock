import jsm_stock_lib
import pandas as pd
import datetime
import jsm
import os

q = jsm.Quotes()
c = jsm.QuotesCsv()
file_type=".csv"
now=datetime.datetime.now()
root_path="./stock_data/monthly_data/"
date_str=now.strftime("%Y%m%d")
#stock_id must be a int
TIME_TYPE=["DAILY","WEEKLY","MONTHLY","YEARLY"]

def read_stock_id(file_name):
    #return pd.read_csv(file_name,encoding="utf-8")
    print(file_name)
    data = pd.read_csv(file_name)
    return data

def download_whole_data(stock_id):
    flag=jsm_stock_lib.int_value_check(stock_id)
    if flag==True:
        data = jsm_stock_lib.get_whole_daily_data(stock_id)

def save_current_month_to_csv(stock_id): #file_name necessary
    flag=jsm_stock_lib.int_value_check(stock_id)
    print(flag)
    if not flag:
        print("int data type error")
        return

    type=jsm_stock_lib.data_type_check(stock_id)
    print(type)
    if type is list:
        for id in stock_id:
            print(id)
            file_name=root_path+str(id)+"-"+date_str+file_type
            c.save_historical_prices(file_name,id)
    elif type is int:
        file_name=root_path+str(stock_id)+"-"+date_str+file_type
        c.save_historical_prices(file_name,stock_id)
    else:
        print("stock data type error")
        exit()

def save_period_to_csv(stock_id,start_date,end_date,time_type): #file_name necessary
    if time_type in TIME_TYPE:
        jsm_type="jsm."+time_type
    else:
        print("set the default value jsm.DAILY")
        jsm_type="jsm.DAILY"

    data_type=jsm_stock_lib.int_value_check(stock_id)
    if data_typ is list:
        for id in stock_id:
            file_name=root_path+id+date_str+file_type
            c.save_historical_prices(file_name,jsm_type,id,start_date,end_date)
    elif type is int:
        file_name=root_path+stock_id+date_str+file_type
        c.save_historical_prices(file_name,jsm_type,stock_id,start_date,end_date)
    else:
        print("stock_id data type error")
        exit()

def save_whole_data(stock_id,time_type):
    if time_type in TIME_TYPE:
        jsm_type="jsm."+time_type
    else:
        print("set the default value jsm.DAILY")
        jsm_type="jsm.DAILY"

    data_type=jsm_stock_lib.int_value_check(stock_id)
    if data_type is list:
        for id in stock_id:
            file_name=id+date_str+file_type
            c.save_historical_prices(file_name,jsm_type,id,all=True)
    elif type is int:
        file_name=stock_id+date_str+file_type
        c.save_historical_prices(file_name,jsm_type,stock_id,all=True)
    else:
        print("stock_id data type error")
        exit()

def download_current_monthly_data(stock_id):
    flag=jsm_stock_lib.int_value_check(stock_id)
    type = jsm_stock_lib.data_type_check(stock_id)
    if flag==True:
        if type =="list":
            for data in stock_id:
                price=jsm_stock_lib.get_current_month_data(data)
        elif type == "int":
            price=jsm_stock_lib.get_current_month_data(stock_id)
        else:
            return None
    else:
        print("stock_id data type error")
        exit()

def check_file(dir_path,file_name_list,update_enable):
    data_type=jsm_stock_lib.data_type_check(file_name_list)
    basename_list=[]
    update_file_list=[]
    if data_type is list:
        for data in file_name_list:
            basename=os.path.basename(data)
            basename_list.append(basename)
    elif data_type is str:
        basename=os.path.basename(file_name_list)
        basename.append(basename)
    else:
        print("file_name_list data type error")
        eit()


    file_list=os.dirlist(dir_path)
    for file in file_list:
        for check_file in basename_list:
            if update_enable:
                update_file_list.append(check_file)
        update_file_list.append(check_file)

    return update_file_list

def main():
    #    file_name="japan-all-stock-prices.csv"
    #    stock_id=read_stock_id(file_name)
    #    print(stock_id)
    stock_file_name="stock_id.txt"
    stock_file_name_test="stock_id_test.txt"
    #stock_id=read_stock_id(stock_file_name)
    stock_id=read_stock_id(stock_file_name_test)
    
    value_data=stock_id.values
    list_data=[]
    for data in value_data:
        #print(data[0])
        list_data.append(data[0])

    data_type=type(list_data)
    #print(list_data)
    #print(data_type)
    #print(list_data)
    save_current_month_to_csv(list_data)
    #download_whole_data(stock_id)

    #save_whole_data()
    print("main function has been called")

if __name__=="__main__":
    main()
