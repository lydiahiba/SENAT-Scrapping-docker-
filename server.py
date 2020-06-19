# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('model/model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True) # data ici c'est le json qu'on va récupérer de insomnia ( il est alimenté dans l'interface insomnia )

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]]) # le exp c'est notre variable qu'on va utilisée dans json dans insomnia pour faire renntrée les valeurs qu'on veux donc c'est comme x ou y c'est variable a remplir 

    # Take the first value of prediction
    output = prediction[0]

    return jsonify(output)

if __name__ == '__main__':
    # app.run(port=8888, host='0.0.0.0', debug=True)
    app.run(port=5000,debug=True,host='0.0.0.0')