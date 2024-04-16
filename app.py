from flask import Flask, render_template, request, jsonify
import joblib


app = Flask(__name__)

# Load your regression and classification models
regression_model = joblib.load('models/regressor_model.joblib')
classification_model = joblib.load('models/classification_model.joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        model_type = request.form['model_type']
        if model_type == 'regression':
            return render_template('input_reg.html')
        elif model_type == 'classification':
            return render_template('input_cla.html')
    return render_template('index.html')

@app.route('/predict_regression', methods=['POST'])
def predict_regression():
    # Get input values from the form
    # Assuming input names are 'feature1', 'feature2', etc.
    feature1 = int(request.form['Month'])
    feature2 = int(request.form['Category'])
    feature3 = int(request.form['Colour'])
    feature4 = int(request.form['Picture Location'])
    feature5 = int(request.form['Model-Photography'])
    feature6 = int(request.form['Product Code'])


    # Add more features as needed

    # Make prediction using the regression model
    prediction = regression_model.predict([[feature1,feature2,feature3,feature4,feature5,feature6]])
    return jsonify({'prediction': prediction[0]})

@app.route('/predict_classification', methods=['POST'])
def predict_classification():
    # Get input values from the form
    # Assuming input names are 'feature1', 'feature2', etc.
    feature1 = int(request.form['Month'])
    feature2 = int(request.form['Category'])
    feature3 = int(request.form['Colour'])
    feature4 = int(request.form['Picture Location'])
    feature5 = int(request.form['Model-Photography'])
    feature6 = int(request.form['Product Code'])

    # Add more features as needed

    # Make prediction using the classification model
    prediction = classification_model.predict([[feature1, feature2,feature3,feature4,feature5,feature6]])  # Adjust based on your features
    # print(prediction)
    if  int(prediction[0]) ==0:
        prediction_label = 'Budget'
    elif  int(prediction[0]) == 1:
        prediction_label = 'Value'
    elif int(prediction[0]==2):
        prediction_label = 'Average'
    else:
        prediction_label = 'Premium'

    return jsonify({'prediction': prediction_label})
    

if __name__ == '__main__':
    app.run(debug=True)
