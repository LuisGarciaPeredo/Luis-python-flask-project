import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('student_performance.pkl', 'rb'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Usuario/Contraseña incorrecto, intente de nuevo.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)


    return render_template('index.html', 
        prediction_text='El rendimiento académico del estudiante es {} donde: Bajo es 0 / Medio es 1 / Alto es 2 .'.format(output),
        Influencers_text='Según data evaluada por el algoritmo, el rendimiento del estudiante se ve influenciado principalmente por: Division5/IMPRESIÓN P, Division1/INTRAPERSONAL, PROMEDIO PONDERADO - Los gráficos se muestran a continuación: ', 
        show_image=1,show_image_1=1
        )



@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    print("reached here")
    data = request.get_json(force=True)
    print("check")
    prediction = model.predict([np.array(list(data.values()))])
    print("modle done")

    output = prediction[0]
    json_output={"output": output}
    print(json_output)

    print("modeldone1")
    return jsonify(json_output)

if __name__ == "__main__":
    app.run(debug=True)
