# Importing essential libraries
from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np

classifier = tf.keras.models.load_model('diabetes_model')

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = classifier.predict(data)
	my_prediction = "Congratuations, You don't have diabetes" if (my_prediction[0][0] < 0.5) else "You Have Diabetes"       

        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)