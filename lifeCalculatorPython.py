# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_lived = int(age)

years_max = 90

years_left = years_max - years_lived

# days_max = years_max * 365

# weeks_max = years_max * 52

# months_max = years_max * 12

# days_lived = years_lived * 365

# weeks_lived = years_lived * 52

# months_lived = years_lived * 12

# days_left = days_max - days_lived

# weeks_left = weeks_max - weeks_lived

# months_left = months_max - months_lived

days_left = years_left * 365

weeks_left = years_left * 52

months_left = years_left * 12

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."

print(message)
