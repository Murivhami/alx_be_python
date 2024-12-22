#!/bin/bash
#Prompt for a single task

Task = input("Enter your task: ")
Time_Bound = input("Is it time-bound? (yes/no): ")
Priority = input("Priority (high/medium/low): ")


match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention!")
    case "low":
        time_bound = "no"
        print(f"Note: '{Task}' is a {Priority} priority task. Consider completing it when you have free time.")
