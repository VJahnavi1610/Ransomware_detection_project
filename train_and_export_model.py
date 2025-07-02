import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Generate synthetic data
n_samples = 1000
np.random.seed(42)
data = {
    'network_traffic': np.random.uniform(0, 1000, n_samples),
    'file_accesses': np.random.randint(0, 100, n_samples),
    'cpu_usage': np.random.uniform(0, 100, n_samples),
    'memory_usage': np.random.uniform(0, 100, n_samples),
    'disk_writes': np.random.randint(0, 1000, n_samples),
    'disk_reads': np.random.randint(0, 1000, n_samples),
    'is_ransomware': np.random.randint(0, 2, n_samples)
}

df = pd.DataFrame(data)

# Save visualizations (optional)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("correlation.png")
plt.close()

# Train/test split
features = ['network_traffic', 'file_accesses', 'cpu_usage', 'memory_usage', 'disk_writes', 'disk_reads']
target = 'is_ransomware'
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "ransomware_detection_model.pkl")
print("Model saved as 'ransomware_detection_model.pkl'")
