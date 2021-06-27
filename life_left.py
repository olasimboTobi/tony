total_life_expectant = 90

your_age = int(input("Enter your age: "))
number_of_years_remaining_for_you = int(total_life_expectant) - your_age
number_of_months_remaining_for_you = (number_of_years_remaining_for_you * int(12))
number_of_days_remaining_for_you = (number_of_years_remaining_for_you * int(365))
number_of_weeks_remaining_for_you = (number_of_years_remaining_for_you * int(52))
print(f"The number of years, months and days remaining for you is as follows: \n")
print(f"YEARS: {number_of_years_remaining_for_you} years \nMONTHS: {number_of_months_remaining_for_you} months \nWEEKS: {number_of_weeks_remaining_for_you} weeks \nDAYS: {number_of_days_remaining_for_you} days")



