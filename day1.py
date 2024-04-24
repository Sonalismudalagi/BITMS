def zellers_formula(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    # Zeller's formula
    q = day
    m = month
    K = year % 100
    J = year // 100

    h = (q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7

    # Converting the result to the corresponding day
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_of_week = days[h]

    return day_of_week

year=int(input("Enter the year"))
if(year>=1000 or year<=9999):
    month=int(input("Enter the month"))
    if(month>=1 or month<=12):
        day=int(input("Enter the day"))
        if(day>=1 or day<=31):
            day_of_week = zellers_formula(day, month, year)
        else:
            print("INcorrect date")
    else:
        print("Incorrect month")
else:
    print("Incorrect year")
print(f"The day of the week for {day}/{month}/{year} is {day_of_week}.")
'''

def is_leap_year(year):
    """
    Check if a year is a leap year
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    # Adjust month value for leap year
    if is_leap_year(year):
        month_adjust = 2
    else:
        month_adjust = 0

    # Zeller's Congruence formula
    q = day
    m = month
    K = year % 100
    J = year // 100

    h = (q + ((13 * (m + 1 + month_adjust)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7

    # Converting the result to the corresponding day
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday"]
    day_of_week = days[h]

    return day_of_week

# Example usage
day = 20
month = 4
year = 2024

day_of_week = zellers_congruence(day, month, year)
print(f"The day of the week for {day}/{month}/{year} is {day_of_week}.")'''