#!/bin/bash
Task = input("Enter you task: ")
Priority = input("Priority (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")

match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention!")
    case "low":
        time_bound = "no"
        print(f"Note: '{Task}' is a {Priority} priority task. Consider completing it when you have free time.")
