from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

model = joblib.load('ransomware_detection_model.pkl')

@app.route('/')
def home():
    prediction_text = session.pop('prediction_text', None)
    return render_template('index.html', prediction_text=prediction_text)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = {
            'network_traffic': [float(request.form['network'])],
            'file_accesses': [int(request.form['file_access'])],
            'cpu_usage': [float(request.form['cpu'])],
            'memory_usage': [float(request.form['memory'])],
            'disk_writes': [int(request.form['disk_write'])],
            'disk_reads': [int(request.form['disk_read'])]
        }

        df = pd.DataFrame(data)
        prediction = model.predict(df)[0]
        label = "Benign" if prediction == 0 else "Ransomware"
        session['prediction_text'] = label  # Store in session temporarily

        return redirect(url_for('home'))  # Redirect after POST (avoids resubmission warning)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
