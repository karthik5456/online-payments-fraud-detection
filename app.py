from flask import Flask, render_template, request
import pickle

# Load the saved model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve values from form inputs
        input_data = [
            float(request.form['feature1']),  # Replace 'feature1' with actual input names
            float(request.form['feature2']),
            # Add more as needed based on your model's input features
        ]
        prediction = model.predict([input_data])[0]
        return render_template('submit.html', prediction_text=f'The prediction is: {prediction}')

if __name__ == "__main__":
    app.run(debug=True)
