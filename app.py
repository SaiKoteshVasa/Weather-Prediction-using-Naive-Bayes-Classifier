from flask import Flask, render_template, request

import pickle
from sklearn.naive_bayes import GaussianNB

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])

def predict():
    map=['Drizzle','Fog','Rain','Snow','Sun']
    if request.method == 'POST':
        month = request.form['month']
        precp = request.form['precp']
        temp_max = request.form['temp_max']
        temp_min = request.form['temp_min']
        wind = request.form['wind']

        data = [[int(month),float(precp),float(temp_max),float(temp_min),float(wind)]]
        
        nbc = pickle.load(open('weather.pkl','rb'))
        prediction = nbc.predict(data)[0]
        prediction=map[prediction]
    
    return render_template('index.html',prediction=prediction) 



if __name__ == '__main__':
    app.run()