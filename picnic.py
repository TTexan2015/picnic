# picnic.py

# Input values
headcount = 35
venue_cost = 120
lunch_cost_per_person = 15
snacks_drinks_miscellaneous_cost_per_person = 5
lunch_people = headcount + 5  # ordering few extras for buffer

# Calculations
total_lunch_cost = lunch_people * lunch_cost_per_person
total_snacks_cost = headcount * snacks_drinks_miscellaneous_cost_per_person
total_cost = venue_cost + total_lunch_cost + total_snacks_cost
per_person_cost = total_cost / headcount

# Output
print("Total cost:", total_cost)
print("Per person cost:", per_person_cost)


