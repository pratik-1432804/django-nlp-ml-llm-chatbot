import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Get current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load dataset safely
csv_path = os.path.join(BASE_DIR, "intents.csv")
data = pd.read_csv(csv_path)

# Features and labels
X_text = data["text"]
y = data["intent"]

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_text)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model
joblib.dump(model, os.path.join(BASE_DIR, "intent_model.pkl"))
joblib.dump(vectorizer, os.path.join(BASE_DIR, "vectorizer.pkl"))

print("✅ Intent model trained and saved successfully")