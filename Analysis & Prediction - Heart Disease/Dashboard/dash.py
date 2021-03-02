from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('home.html')

# Data
@app.route('/dataset', methods=['POST','GET'])
def dataset():
    return render_template('dataset.html')

# Visual
@app.route('/visualize', methods=['POST','GET'])
def visualize():
    return render_template('visual.html')

# Predict
@app.route('/predict', methods=['POST','GET'])
def predict():
    return render_template('predict.html')

# Result
@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        input = request.form

        df_predict = pd.DataFrame({
            'Age':[input['Age']],
            'Gender':[input['Gender']],
            'ChestPain':[input['ChestPain']],
            'RestingBloodPressure':[input['RestingBloodPressure']],
            'Cholesterol':[input['Cholesterol']],
            'FastingBloodSugar':[input['FastingBloodSugar']],
            'RestingECG':[input['RestingECG']],
            'MaxHeartRateAchieved':[input['MaxHeartRateAchieved']],
            'ExerciseInducedAngina':[input['ExerciseInducedAngina']],
            'Oldpeak':[input['Oldpeak']],
            'Slope':[input['Slope']],
            'MajorVessels':[input['MajorVessels']],
            'Thalassemia':[input['Thalassemia']]
        })

        prediksi = model.predict_proba(df_predict)[0][1]

        if prediksi < 0.5:
            hasil = 'NO HEART DISEASE!'
        else:
            hasil = 'HEART DISEASE! SEEK HELP!'

        return render_template('result.html', data=input, pred=hasil)

if __name__ == '__main__':
    filename = 'C:/Users/hapis/OneDrive/Documents/Data Science/Final Project/Dashboard/Random Forest for Heart Disease Final.sav'
    model = pickle.load(open(filename,'rb'))
    app.run(debug=True)
