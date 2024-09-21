
total_population = 1001176
total_shooting_incidents = 4

# Basic probability of shooting
probability_of_shooting = total_shooting_incidents / total_population
print(f"Basic probability of a school shooting in San Jose: {probability_of_shooting:.8f}")

# Population by race
population_by_race = {
    'Asian': 381796,
    'White': 320311,
    'Other race': 132471,
    'Two or more races': 124101,
    'Black or African': 29374,
    'Native American': 8427,
    'Hawaiian': 4696
}

# Poverty rates by race
poverty_rates = {
    'Asian': 7.3,
    'White': 6.3,
    'Other race': 10.87,
    'Two or more races': 8.45,
    'Black or African': 13.34,
    'Native American': 12.07,
    'Hawaiian': 6.49
}

# Total gun owners
total_gun_owners = 257000

# Adjusted probabilities factoring in gun ownership and poverty rates
adjusted_probabilities_by_race = {}
for race, population in population_by_race.items():
    poverty_rate = poverty_rates.get(race, 0) / 100  # Convert to decimal
    gun_ownership_factor = total_gun_owners / total_population
    base_probability = total_shooting_incidents / population
    
    # Adjust probability based on poverty rate and gun ownership
    adjusted_probability = base_probability * (1 + poverty_rate) * (1 + gun_ownership_factor)
    adjusted_probabilities_by_race[race] = adjusted_probability

# Display adjusted probabilities
for race, adjusted_probability in adjusted_probabilities_by_race.items():
    print(f"Adjusted probability of a school shooting for {race}: {adjusted_probability:.8f}")