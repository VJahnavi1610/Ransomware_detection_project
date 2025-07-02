Ransomware Detection Web App

This project is a web-based application that detects ransomware activity using a trained **Random Forest Classifier** on synthetic system behavior data (e.g., network traffic, CPU usage, memory, etc.).

Users can input system metrics, and the app will predict whether the behavior is **Benign** or **Ransomware**.

🛠️ Setup Instructions

📦 Prerequisites

Make sure you have the following installed on your system:

* [Python 3.8+](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/)
* Git (optional, for cloning)

🔧 Step-by-Step Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/ransomware-detection-app.git
   cd ransomware-detection-app
   ```

2. **(Optional but Recommended) Create a virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # For Windows
   source .venv/bin/activate  # For Linux/Mac
   ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not available, manually install:

   ```bash
   pip install flask pandas numpy matplotlib seaborn scikit-learn joblib
   ```

4. **Train the model (Optional: Already included as .pkl file)**

   If you want to retrain the model:

   ```bash
   python train_model.py
   ```

   This will generate `ransomware_detection_model.pkl`.

5. **Run the Flask app**

   ```bash
   python app.py
   ```

6. **Open in your browser**

   Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 💡 Features

* Beautiful, responsive HTML UI using custom CSS
* Real-time prediction of ransomware activity
* Trained on synthetic behavioral data
* Handles both desktop and mobile views


## 🧠 Model Info

* **Algorithm**: Random Forest Classifier
* **Training Data**: Synthetic data simulating CPU, memory, file access, etc.
* **Target**: `is_ransomware` (0 = Benign, 1 = Ransomware)


