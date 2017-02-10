from jsm_stock_lib import *
import pandas as pd
import datetime
import jsm
import os
import time
import calendar
from japan_stock_id_divided import *
from DAILY_STOCK_MONITOER import *
from quandl_data_downlaod import *

q = jsm.Quotes()
c = jsm.QuotesCsv()
FILE_TYPE=".csv"
now=datetime.datetime.now()
ROOT_PATH="/Users/zhonghan/workspace/japan_stock_analysis/python_stock/stock_data/"
MONTHLY_DIR_PATH="./stock_data/monthly_data/"
date_str=now.strftime("%Y%m%d")
#stock_id must be a int
TIME_TYPE=["DAILY","WEEKLY","MONTHLY","YEARLY"]

def read_stock_csv_id(file_name):
    #return pd.read_csv(file_name,encoding="utf-8")
    print(file_name)
    data = pd.read_csv(file_name)
    return data

def download_whole_data(stock_id):
    #flag=jsm_stock_lib.int_value_check(stock_id)
    flag=int_value_check(stock_id)
    if flag==True:
        #data = jsm_stock_lib.get_whole_daily_data(stock_id)
        data = get_whole_daily_data(stock_id)

def save_current_month_to_csv(stock_id): #file_name necessary
    #flag=jsm_stock_lib.int_value_check(stock_id)
    flag=int_value_check(stock_id)
    print(flag)
    if not flag:
        print("int data type error")
        return

    #type=jsm_stock_lib.data_type_check(stock_id)
    type=data_type_check(stock_id)
    print(type)
    if type is list:
        for id in stock_id:
            print(id)
            file_name=MONTHLY_DIR_PATH+str(id)+"-"+date_str+FILE_TYPE
            c.save_historical_prices(file_name,id)
    elif type is int:
        file_name=MONTHLY_DIR_PATH+str(stock_id)+"-"+date_str+FILE_TYPE
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
            file_name=MONTHLY_DIR_PATH+id+date_str+FILE_TYPE
            c.save_historical_prices(file_name,id,jsm_type,start_date,end_date)
    elif type is int:
        file_name=MONTHLY_DIR_PATH+stock_id+date_str+FILE_TYPE
        c.save_historical_prices(file_name,stock_id,jsm_type,start_date,end_date)
    else:
        print("stock_id data type error")
        exit()

def last_day_of_month(date):
    _,last_day=calendar.monthrange(date.year,date.month)
    last_date=datetime.date(date.year,date.month,last_day)
    return last_date
    '''
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)
    '''


def save_whole_data(stock_id,time_type): #stock_id is a list #test ok
    whole_data_path="./stock_data/whole_data/"
    start_time = datetime.date(2000,1,1)
    start_year=start_time.year
    start_month=start_time.month
    start_day=start_time.day

    now_date=datetime.datetime.now().date()
    end_month=now_date.month
    end_year=now_date.year
    end_day=last_day_of_month(datetime.date(now.year,now.month-1,1))
    time_period=[[],[]]
    file_name_suffix = []
    num_year=end_year-start_year+1
    year_list=[]

    #the year before the current year untill the start year
    for year in range(start_year,end_year):
        year_list.append(year)
        if not os.path.exists(ROOT_PATH+str(year)):
            os.mkdir(ROOT_PATH+str(year))
        for i in range(1,13):
            time_period[0].append(datetime.date(year,i,1))
            last_day=last_day_of_month(datetime.date(year,i,1))
            time_period[1].append(last_day)
            file_name_suffix.append(last_day.strftime("%Y%m%d"))
        # current year processing
    for month in range(1,end_month):
        last_day=last_day_of_month(datetime.date(end_year,month,1))
        start_day=datetime.date(end_year,month,1)
        time_period[0].append(start_day)
        time_period[1].append(last_day)
        file_name_suffix.append(last_day.strftime("%Y%m%d"))

    print(time_period[0])
    print(time_period[1])
    #print(file_name_suffix)
    #now_str=now_date.timefstr("%Y%m%d")

    jsm_type=jsm_type_check(time_type)
    print(jsm_type)

    data_type=data_type_check(stock_id)
    if data_type is list:
        for id in stock_id:
            print("stock_id:"+str(id))
            for data1 in time_period[1]:
                index=time_period[1].index(data1)
                print(data1)
                data_str=data1.strftime("%Y%m%d")
                print(data_str)
                print("index:"+str(index))

                print(data_str)
                save_folder=ROOT_PATH+str(data1.year)+"/"
                file_name=str(id)+"-"+data_str+FILE_TYPE
                file_path=save_folder+file_name
                if os.path.exists(file_path):
                    print(file_path+" exists!! skip!!")
                else:
                    print("stock download")
                    c.save_historical_prices(file_path,id,jsm_type,time_period[0][index],data1)

                while not os.path.exists(file_path):
                    time.sleep(1)

                #print(file_path)
                print("start_time:")
                print(time_period[0][index])
                print("end_time:")
                print(data1)
                print("next stok download:")
                #print(jsm_type)
        print(time_period[1])


    #elif isinstance(data_type,(int,np.int64):
    #    file_name=stock_id+date_str+FILE_TYPE
    #    c.save_historical_prices(file_name,jsm_type,stock_id,all=True)
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

def check_file(dir_path,file_name_list,update_enable): #update_enable:1 update 0: not update
    data_type=data_type_check(file_name_list)
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
        exit()

    file_list=os.dirlist(dir_path)
    for file in file_list:
        for check_file in basename_list:
            if update_enable:
                update_file_list.append(check_file)
        update_file_list.append(check_file)

    return update_file_list

def downlaod_stock_data(save_type):
    print("not implemented!!")

def main():
    downlaod_stock_data()
    main_monitor_loop()
    
"""
    type1="nikkei225"
    stock_dataframe=read_stock_id(type1)
    print(len(stock_dataframe["SC"])) # nkkei 225
    stock_id=stock_dataframe["SC"]
    list_data=[]
    for data in stock_id:
        list_data.append(data)
    print(len(list_data))

    #save_current_month_to_csv(list_data)

    print("download the whole data!!")
    #download_whole_data(list_data)
    #save_whole_data()

    print("main function has been called")
"""

"""
    #old version source code (not used)
    #    file_name="japan-all-stock-prices.csv"
    #    stock_id=read_stock_csv_id(file_name)
    #    print(stock_id)
    stock_file_name="stock_id.txt"
    stock_file_name_test="stock_id_test.txt"
    #stock_id=read_stock_csv_id(stock_file_name)
    stock_id=read_stock_csv_id(stock_file_name_test)

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
"""

if __name__=="__main__":
    main()
