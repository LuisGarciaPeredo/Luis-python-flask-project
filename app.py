import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('student_performance.pkl', 'rb'))

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
        prediction_text='student_performance is {} where low:0, medium:1 and high:2'.format(output),
        Influencers_text='If student performace is poor then it is mainly due to Prom_Ponderado, Impres/Division5, Intra/Division1 - Graphs are shown below ', 
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
