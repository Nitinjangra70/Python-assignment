# Project: Daily Calorie Tracker
# Name : Nitin
# Roll no : 2501730221
# Course : B.tech CSE(AIML)
# Subject : Programming For Problem Solving Using Python 
# Date: 10th November 2025

print("  Welcome to the Calorie Tracker! ")

# Ask how many meals were eaten today
num_meals = input("How many meals did you eat today? ")

# Convert input to an integer safely
num_meals = int(num_meals)

# Create empty lists to store meal names and calories
meal_names = []
calories = []

# Loop to take meal details
for i in range(num_meals):
    print("\nMeal", i + 1)
    meal = input("Enter meal name: ")
    cal = input("Enter calories for this meal: ")

    # Convert calories to float number
    cal = float(cal)

    # Add values to lists
    meal_names.append(meal)
    calories.append(cal)

# Calculate total and average calories
total = sum(calories)
average = total / num_meals

# Ask the user for their daily limit
daily_limit = float(input("\nEnter your daily calorie limit: "))

# Display a simple report
print("\n------------------------------------")
print("Your Daily Calorie Summary")
print("------------------------------------")
print("Meal Name\tCalories")
print("------------------------------------")

for i in range(num_meals):
    print(meal_names[i], "\t", calories[i])

print("------------------------------------")
print("Total:\t\t", total)
print("Average:\t", round(average, 2))
print("------------------------------------")

# Check if user went over the daily limit
if total > daily_limit:
    print("⚠️ You have exceeded your daily calorie limit!")
else:
    print("✅ You are within your daily calorie limit!")

# Ask if user wants to save data to file
save = input("\nDo you want to save this report to a file? (yes/no): ")

if save.lower() == "yes":
    now = datetime.datetime.now()

    # Open a file for writing
    with open("calorie_log.txt", "w") as file:
        file.write("Calorie Tracker Report\n")
        file.write("Date and Time: " + str(now) + "\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("------------------------------------\n")

        for i in range(num_meals):
            file.write(meal_names[i] + "\t" + str(calories[i]) + "\n")

        file.write("------------------------------------\n")
        file.write("Total:\t" + str(total) + "\n")
        file.write("Average:\t" + str(round(average, 2)) + "\n")

        if total > daily_limit:
            file
