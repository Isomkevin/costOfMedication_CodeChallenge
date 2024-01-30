Python's fun:😀

Dr Dottel is an expert in treating mylosis disease. She administers 4 tablets for pain relief every day to each of her infected patients. She knows that patients with this disease cannot live beyond 90 years.

Assume that each table costs Kshs 1799.65;

Write a simple program which could be used  to compute the cost
of medication for this critical tablets if a patient lives to be be 90 years.

Note.
1 year  =  365 days
Patient1 is  78 years
Patient2 is 12 years


AgeofDeath = 90
NumOfTablet_perDay = 4
tablet_price = 1799.65

RemainingYears = AgeOfDeath * CurrentAge
Patient_RemainingDays => RemainingYears * DaysInYear


perDay_price => tablet_price * NumOfTablet_perDay

Formula => perDay_price * Patient_RemainingDays


AgeofDeath = 90
NumOfTablet_perDay = 4
tablet_price = 1799.65


def cost_of_medication(AgeOfPatient, NumOfTablet_perDay, tablet_price)

RemainingYears = AgeOfDeath * CurrentAge
Patient_RemainingDays => RemainingYears * DaysInYear


perDay_price => tablet_price * NumOfTablet_perDay


cost = perDay_price * Patient_RemainingDays
return cost



cost_of_medication(AgeOfPatient) = cost of medication

