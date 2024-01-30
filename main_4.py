
cost_per_tablet = 1799.65

def cost_of_medication(patientAge, cost_per = cost_per_tablet):
    tablets_Quantity = tabletsNeeded_Quantity(patientAge)
    total_Cost_of_tablets = tablets_Quantity * cost_per

    return total_Cost_of_tablets


def tabletsNeeded_Quantity(patientAge: int):
    tablets_per_day: int = 4
    deathDuration: int = deathDuration_days(patientAge)
    totalTabletsNeeded: int = deathDuration * tablets_per_day

    return totalTabletsNeeded


def deathDuration_days(current_age: int):
    lifespan: int = 90
    days_in_year = 365

    remaining_years = lifespan - current_age
    remaining_days = remaining_years * days_in_year

    return remaining_days


total_medicationCost = cost_of_medication(78)
print(total_medicationCost)