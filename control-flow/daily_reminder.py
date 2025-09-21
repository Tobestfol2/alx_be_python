# This script reminds the user about a single task based on its priority and time sensitivity.

# Prompt the user for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Enter the task's priority (high, medium, low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Use a match-case statement to handle priority and a variable to build the message
reminder = ""
match priority:
    case 'high':
        reminder = f"Reminder: '{task}' is a high-priority task"
    case 'medium':
        reminder = f"Reminder: '{task}' is a medium-priority task"
    case 'low':
        reminder = f"Reminder: '{task}' is a low-priority task"
    case _:
        reminder = f"Reminder: '{task}' is a task with an unspecified priority"

# Use an if statement to modify the message if the task is time-bound
if time_bound == 'yes':
    reminder += " that requires immediate attention today!"

# Print the final reminder
print(reminder)
