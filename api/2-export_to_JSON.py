#!/usr/bin/python3
"""
Employee TODO Progress Module with JSON Export

This module fetches an employee's TODO list progress using a REST API and
exports the data to a JSON file. It retrieves employee information and their
associated tasks, then saves the data in the specified format.

The module uses the JSONPlaceholder API (https://jsonplaceholder.typicode.com)
for demonstration purposes.

Usage:
    python todo_progress_json.py <employee_id>

Dependencies:
    - requests library (install via pip install requests)
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch an employee's TODO list progress and export to JSON.

    This function retrieves employee information and their TODO list from the
    API, then exports the data to a JSON file.

    Args:
        employee_id (int): The ID of the employee to fetch information for.

    Returns:
        None. The function exports data to a JSON file.

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
    username = employee_data['username']

    # Get TODO list for the employee
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list. "
              f"Status code: {todos_response.status_code}")
        return

    todos = todos_response.json()

    # Prepare data for JSON export
    json_data = {
        str(employee_id): [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            }
            for todo in todos
        ]
    }

    # Export data to JSON
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    # Command-line argument parsing and error handling
    if len(sys.argv) != 2:
        print("Usage: python todo_progress_json.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    # Call the main function
    get_employee_todo_progress(employee_id)
