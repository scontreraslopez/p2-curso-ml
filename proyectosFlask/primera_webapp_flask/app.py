from utilities import predict_pipeline
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',val='')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        enginesize = float(request.form['ENGINESIZE'])
        cylinders = float(request.form['CYLINDERS'])
        fuelconsumption_comb = float(request.form['FUELCONSUMPTION_COMB'])
        # Comprobamos que tenemos todos los datos
        if enginesize=='' or cylinders=='' or fuelconsumption_comb=='':
            return render_template('home.html',val='Todos los campos son obligatorios')
        #Solicitamos predicción
        my_prediction = predict_pipeline(enginesize,cylinders,fuelconsumption_comb)
        #Temporalmente mostramos por consola predicción
        print(my_prediction)
        #Mostrar html con el resultado
        return render_template('home.html',
            val=f'Consumo estimado de CO2 de {my_prediction} para los datos: Motor={enginesize};Cilindros={cylinders};Consumo={fuelconsumption_comb}.')

if __name__ == '__main__':
    app.run(debug=True)