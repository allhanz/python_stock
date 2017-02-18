# the example for study
# Create first network with Keras
from keras.models import Sequential, model_from_json
from keras.layers import Dense
import numpy as np
from read_csv_to_pandas import *
import os
import json


f_model="./ML_model"
f_log="./log/ML_model_log"

def build_ML_model(input_data):

    # fix random seed for reproducibility
    seed = 7
    np.random.seed(seed)

    # load pima indians dataset
    dataset = np.loadtxt("./test_data/pima-indians-diabetes.csv", delimiter=",")
    print()
    # split into input (X) and output (Y) variables
    X = dataset[:,0:8]
    Y = dataset[:,8]

    # create model
    model = Sequential()
    model.add(Dense(20, input_dim=8, init='uniform', activation='relu'))
    model.add(Dense(8, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform', activation='sigmoid'))

    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Fit the model
    model.fit(X, Y, nb_epoch=200, batch_size=10,  verbose=2)

    # evaluate the model
    scores = model.evaluate(X, Y)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    # calculate predictions
    predictions = model.predict(X)

    # round predictions
    #rounded = [round(x) for x in predictions]
    rounded = np.round(predictions)
    print(len(rounded))

def save_trained_ML_model(model_data,file_name): #json format
    json_str=model_data.to_json()
    open(os.path.join(f_model,file_name,"w").write(json)
    print("not implemented!!")

def load_ML_model(model_data,file_name): # load from json file
    ML_model=model_from_json(open(os.path.join(f_model,file_name),"r").read())
    return ML_model

def get_ML_input_data(stock_id_list,all):
    stock_data=get_one_stock_whole_data(stock_id_list,all)
    return stock_data

def data_pre_process(stock_data_list):
    #stock_data_list=[{""}]
    print("not implemented!!")

def main():
    if os.path.exists(f_log):
        os.mkdir(f_log)

    stock_id_list=["1419","1420"]
    all_type=False
    input_data=get_ML_input_data(stock_id_list,all_type)
    print(input_data)

if __name__=="__main__":
    main()
    #build_ML_model()
