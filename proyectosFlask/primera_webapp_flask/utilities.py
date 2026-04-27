import pickle
import pandas as pd
import sklearn

with open('models/pipeline.pickle', 'rb') as f:
    loaded_pipe = pickle.load(f)
    
def predict_pipeline(enginesize,cylinders,fuelconsumption_comb):
    return loaded_pipe.predict(pd.DataFrame([[enginesize,cylinders,fuelconsumption_comb]], columns=['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']))[0]

#Comentar cuando ya tengamos la aplicación hecha para evitar redundancia
if __name__=="__main__":
    #Prueba que debería de devolver 185.92638775794967
    predictions = predict_pipeline(1.4, 4.0, 7.8)
    print(predictions)