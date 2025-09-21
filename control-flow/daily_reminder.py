task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
         reminder = f"Reminder: '{task}' is a HIGH priority task."
         if time_bound == "yes":
              reminder += " It requires immediate attention today!"
    case "medium":
            reminder = f"Reminder: '{task}' is a MEDIUM priority task."
            if time_bound == "yes":
                reminder += " try to complete it soon."          
    case "low":
            reminder = f"Reminder: '{task}' is a LOW priority task."
            if time_bound == "yes":
                reminder += " But keep in mind it still has a deadline."
            else:
                reminder += " consider completing it when you have freetime."
    case _:
            reminder = "Invalid priority level. Please enter high, medium, or low."
print(reminder)