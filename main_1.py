
ageofDeath = 90
numOfTablet_daily = 4
cost_of_tablet = 1799.65
daysInYear = 365

def cost_of_medication(currentAge, numOfDailyTablet = numOfTablet_daily, tablet_price = cost_of_tablet, yearDays = daysInYear ,deathAge = ageofDeath):

    patient_RemainingYears = deathAge - currentAge
    patient_RemainingDays = patient_RemainingYears * yearDays

    perDay_price = tablet_price * numOfDailyTablet


    cost = perDay_price * patient_RemainingDays

    return cost



medicationCost = cost_of_medication(78)
print(medicationCost)