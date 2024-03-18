import random

# Generate a random amount between 0.0000300 and 0.0000315, rounded to 8 decimal places
amount = round(random.uniform(0.0000300, 0.0000315), 8)

# Print the generated amount
print(amount)
