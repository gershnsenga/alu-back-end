#!/usr/bin/env python3
"""
Employee TODO Progress Module

This module provides functionality to fetch and display an employee's TODO list
progress using a REST API. It retrieves employee information and their
associated tasks, then calculates and presents the progress in a specified
format.

The module uses the JSONPlaceholder API (https://jsonplaceholder.typicode.com)
for demonstration purposes.

Usage:
    python todo_progress.py <employee_id>

Dependencies:
    - requests library (install via pip install requests)
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetch and display an employee's TODO list progress.

    This function retrieves employee information and their TODO list from the
    API, calculates the progress, and displays it in the specified format.

    Args:
        employee_id (int): The ID of the employee to fetch information for.

    Returns:
        None. The function prints the results to stdout.

    Raises:
        No exceptions are raised directly, but error messages are printed to
        stdout if API requests fail or if the employee ID is invalid.
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    if employee_response.status_code != 200:
        print(f"Error: Unable to fetch employee data. "
              f"Status code: {employee_response.status_code}")
        return

    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Get TODO list for the employee
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list. "
              f"Status code: {todos_response.status_code}")
        return

    todos = todos_response.json()
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Display the progress
    print(f"Employee {employee_name} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")

    # Display completed tasks
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    # Command-line argument parsing and error handling
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    # Call the main function
    get_employee_todo_progress(employee_id)
