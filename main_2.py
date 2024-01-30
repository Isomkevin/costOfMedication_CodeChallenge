class MedicationCostCalculator:
    def __init__(self, tablet_price=1799.65, num_of_tablet_daily=4, days_in_year=365, age_of_death=90):
        self.tablet_price = tablet_price
        self.num_of_tablet_daily = num_of_tablet_daily
        self.days_in_year = days_in_year
        self.age_of_death = age_of_death

    def cost_of_medication(self, current_age):
        patient_remaining_years = self.age_of_death - current_age
        patient_remaining_days = patient_remaining_years * self.days_in_year
        per_day_price = self.tablet_price * self.num_of_tablet_daily
        cost = per_day_price * patient_remaining_days
        return cost

    def set_tablet_price(self, new_tablet_price):
        self.tablet_price = new_tablet_price

    def set_num_of_tablet_daily(self, new_num_of_tablet_daily):
        self.num_of_tablet_daily = new_num_of_tablet_daily

    def set_age_of_death(self, new_age_of_death):
        self.age_of_death = new_age_of_death


# Test the MedicationCostCalculator class

def test_medication_cost():
    # Creating an instance of MedicationCostCalculator
    calculator = MedicationCostCalculator()

    # Calculate medication cost for a patient of 78 years old
    medication_cost = calculator.cost_of_medication(78)
    print(medication_cost)
    assert medication_cost == 31529868.0  # Expected cost for a patient of 78 years old

    # Changing tablet price, number of tablets daily, and age of death
    calculator.set_tablet_price(2000)  # Change tablet price
    calculator.set_num_of_tablet_daily(5)  # Change number of tablets daily
    calculator.set_age_of_death(85)  # Change age of death

    # Recalculate medication cost for a patient of 78 years old after changes
    medication_cost_after_changes = calculator.cost_of_medication(78)
    assert medication_cost_after_changes == 30572250.0  # Expected cost after changes for a patient of 78 years old

    print("All tests passed successfully!")


# Run the tests
test_medication_cost()
# calculator = MedicationCostCalculator()

# # Calculate medication cost for a patient of 78 years old
# medication_cost = calculator.cost_of_medication(78)
# print(medication_cost)


