#!/bin/bash
single_task = input("Enter you task: ")
priority = input("Priority (high/medium/low): ")
time_sensitive = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_sensitive == "yes":
            print(f"Reminder: '{single_task}' is a {priority} priority task that requires immediate attention!")
    case "low":
        time_sensitive = "no"
        print(f"Note: '{single_task}' is a {priority} priority task. Consider completing it when you have free time.")
