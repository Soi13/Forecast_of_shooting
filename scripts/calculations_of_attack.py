# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Hypothetical dataset with factors
data = {
    'crime_rate': [10, 3, 8, 10, 2, 6, 7, 9, 1, 4],
    'gun_ownership': [0.3, 0.25, 0.35, 0.4, 0.2, 0.32, 0.33, 0.37, 0.22, 0.28],
    'mental_health_resources': [3, 4, 2, 1, 5, 2, 3, 1, 4, 5],
    'school_security': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'historical_incidents': [1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    'school_attack': [1, 1, 1, 1, 0, 0, 1, 1, 0, 0]  # 1: Attack, 0: No Attack
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Define features (X) and target (y)
X = df[['crime_rate', 'gun_ownership', 'mental_health_resources', 'school_security', 'historical_incidents']]
y = df['school_attack']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Predicting the probability of an attack in a specific city with given parameters
city_data = np.array([[7, 0.3, 3, 1, 1]])  # Example city data
probability = model.predict_proba(city_data)
print(f"Probability of school attack: {probability[0][1] * 100:.2f}%")