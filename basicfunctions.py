#Variables that withold a strings:
name = "Johnny Appleseed"
current_occupation = "apple picker in his family's orchard."

#Variables that withold integers:
age = 25
hourly_wage = 14.80
hours_per_week = 40
apples_picked_per_day = 145
days_worked_per_week = 5 

#Variables that calculate annual wage/apples picked:
annual_wage = ((hourly_wage * hours_per_week) * 52)
annual_apples = ((apples_picked_per_day * days_worked_per_week) * 52)

#Print statements:
print("Hello, this is " + name + "!")
print("He is " + str(age) + " years old.")
print("He is currenty employed as an " + current_occupation)
print(f"He picks {annual_apples} apples and makes ${annual_wage} per year.")
