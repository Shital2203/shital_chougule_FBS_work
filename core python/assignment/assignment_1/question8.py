# Program to convert days into years, weeks, and days

# Input: total number of days
days = int(input("Enter the number of days: "))

# Calculations
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
days_left = remaining_days % 7

# Output
print(f"{days} days = {years} year(s), {weeks} week(s), and {days_left} day(s)")
