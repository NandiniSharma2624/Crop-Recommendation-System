from flask import Flask, render_template, request, redirect, jsonify
from model import predict_crop

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loading', methods=['POST'])
def loading():
    #collectind data from webpage
    data = [
        float(request.form['nitrogen']),
        float(request.form['phosphorus']),
        float(request.form['potassium']),
        float(request.form['temperature']),
        float(request.form['humidity']),
        float(request.form['ph']),
        float(request.form['rainfall'])
    ]
    # Store data in session or a temporary storage if needed
    # For simplicity, let's redirect to result directly
    result = predict_crop(data)
    return jsonify({'crop': result})
    #return redirect(url_for('result', data=data))


@app.route('/predict', methods=['POST'])
def predict():
    data = [
        float(request.form['nitrogen']),
        float(request.form['phosphorus']),
        float(request.form['potassium']),
        float(request.form['temperature']),
        float(request.form['humidity']),
        float(request.form['ph']),
        float(request.form['rainfall'])
    ]
    result = predict_crop(data)
    return jsonify({'crop': result})

'''@app.route('/result')
def result():
    # Get data from query parameters
    data = request.args.getlist('data', type=float)
    if not data:
        return redirect(url_for('index'))

    # Predict crop
    result = predict_crop(data)
    return render_template('result.html', result=result)'''

if __name__ == '__main__':
    app.run(debug=True)
