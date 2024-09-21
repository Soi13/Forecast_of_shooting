import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Step 1: Prepare your data
data = {
    'Year': [1994, 1995, 1999, 2000, 2017, 2018, 2021, 2022],  # Add years with no shootings
    'Population': [782248, 838000, 894943, 894943, 1037082, 1034877, 981214, 972082],  # Same population for simplicity
    'Gun_Owners': [257000, 257000, 257000, 257000, 257000, 257000, 257000, 257000],  # Same gun ownership
    'Asian_Population': [381796, 381796, 381796, 381796, 381796, 381796, 381796, 381796],
    'White_Population': [320311, 320311, 320311, 320311, 320311, 320311, 320311, 320311],
    'Black_African_Population': [29374, 29374, 29374, 29374, 29374, 29374, 29374, 29374],
    'Poverty_Rate_Black_African': [13.34, 13.34, 13.34, 13.34, 13.34, 13.34, 13.34, 13.34],
    'Poverty_Rate_Hispanic': [9.36, 9.36, 9.36, 9.36, 9.36, 9.36, 9.36, 9.36],
    'Poverty_Rate_Asian': [7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3,],
    # Add other relevant factors here
    'Shooting_Occurred': [1, 0, 1, 0, 1, 0, 1, 0]  # 1 = shooting occurred, 0 = no shooting
}

# Step 2: Create a DataFrame
df = pd.DataFrame(data)

# Step 3: Define features (X) and target (y)
X = df[['Population', 'Gun_Owners', 'Asian_Population', 'White_Population', 'Black_African_Population', 'Poverty_Rate_Black_African', 'Poverty_Rate_Hispanic', 'Poverty_Rate_Asian']]
y = df['Shooting_Occurred']

# Step 4: Train-test split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Initialize and train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Get the predicted probabilities for the test set
probabilities = model.predict_proba(X_test)

# The second column represents the probability of class "1" (shooting occurring)
shooting_probabilities = probabilities[:, 1]

# Step 7: Display the shooting probabilities for each test case
for i, prob in enumerate(shooting_probabilities):
    print(f"Test case {i+1}: Probability of a school shooting occurring = {prob * 100:.2f}%")

# Example of predicting the probability for a specific new input data
input_data = [[1001176, 257000, 381796, 320311, 29374, 13.34, 9.36, 7.3]]  # New input features
shooting_probability = model.predict_proba(input_data)[0][1]

print(f"\nProbability of a school shooting for new data: {shooting_probability * 100:.2f}%")
