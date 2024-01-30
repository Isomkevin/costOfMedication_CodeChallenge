# Cost per tablet
cost_per_tablet = 1799.65

# Function to calculate medication cost
def calculate_medication_cost(age):
    # Assuming each patient lives up to 90 years
    deathAge = 90
    remaining_years = deathAge - age
    remaining_days = remaining_years * 365

    # Number of tablets taken per day
    tablets_per_day = 4

    # Total tablets needed
    total_tablets = tablets_per_day * remaining_days

    # Total cost of medication
    total_cost = total_tablets * cost_per_tablet
    return total_cost







### Testing CodeBase
# Patient 1 information
patient1_age = 78
patient1_cost = calculate_medication_cost(patient1_age)

print(f"Total cost of medication for Patient 1: Kshs {patient1_cost:.2f}")

# Patient 2 information
patient2_age = 12
patient2_cost = calculate_medication_cost(patient2_age)

print(f"Total cost of medication for Patient 2: Kshs {patient2_cost:.2f}")
