import json
import pickle
import numpy as np
__locations =None
__data_columns=None
__model=None


def get_location_names():
    return __locations
def load_saved_artefacts():
    print("loading the saved artefacts.....start")
    global __data_columns
    global __locations
    global __model
    with open("./artefacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]
    with open("./artefacts/bangalore_house_prices_model.pickle",'rb') as f:
        __model=pickle.load(f)
    print("loading of artefacts is done")

#get location should read the column containing location


#---------------------------------------------------------------------------------------------------------------------------------------------



#now we will write a routine that will give the predicted wstimated price of a house absased on a area


def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1



    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1

    return round(__model.predict([x])[0],2)




if __name__=="__main__":
    load_saved_artefacts()
    print(get_location_names())
    print(get_estimated_price('1sr Phase JP Nagar',1000,3,3))
    print(get_estimated_price('Kalhali', 1000, 5, 3))
