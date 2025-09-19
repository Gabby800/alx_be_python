# daily_reminder.py

# Prompt user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match case
match priority:
    case "high":
        reminder = f"'{task}' is a HIGH priority task."
    case "medium":
        reminder = f"'{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"'{task}' is a LOW priority task."
    case _:
        reminder = f"'{task}' has an UNRECOGNIZED priority level."

# Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " You can schedule it based on your free time."

# ✅ Print the customized reminder (final output to user)
print("Reminder:", reminder)
