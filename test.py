import pandas as pd

# Population data by race
population_data = {
    'Race': ['Asian', 'White', 'Other race', 'Two or more races', 'Black or African American', 'Native American', 'Native Hawaiian or Pacific Islander'],
    'Population': [381796, 320311, 132471, 124101, 29374, 8427, 4696]
}

df = pd.DataFrame(population_data)

# Calculate total population
total_population = df['Population'].sum()
print(f"Total population: {total_population}")

# Assuming you have the total number of school shootings in San Jose
total_shooting_incidents = 4  # Replace with actual value from your dataset

# Calculate the basic probability of a school shooting
probability_of_shooting = total_shooting_incidents / total_population
#print(f"Probability of a school shooting: {probability_of_shooting:.8f}")

# If you want to focus on a specific race, calculate a conditional probability
asian_population = df[df['Race'] == 'Asian']['Population'].values[0]
probability_of_shooting_asian = total_shooting_incidents / asian_population
#print(f"Probability of a school shooting for Asian population: {probability_of_shooting_asian:.8f}")

print(total_population)