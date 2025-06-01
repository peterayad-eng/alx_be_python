task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
print(f"")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a high priority task Consider completing it")
        else: print(f"Please enter valid time bound")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a medium priority task Consider completing it")
        else: print(f"Please enter valid time bound")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else: print(f"Please enter valid time bound")
    case _:
        print(f"Please enter valid priority")

