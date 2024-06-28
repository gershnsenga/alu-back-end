#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
        # Base URL for the API
            base_url = "https://jsonplaceholder.typicode.com"

                # Get employee information
                    employee_response = requests.get(f"{base_url}/users/{employee_id}")
                        if employee_response.status_code != 200:
                                    print(f"Error: Unable to fetch employee data. Status code: {employee_response.status_code}")
                                            return

                                            employee_data = employee_response.json()
                                                employee_name = employee_data['name']

                                                    # Get TODO list for the employee
                                                        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
                                                            if todos_response.status_code != 200:
                                                                        print(f"Error: Unable to fetch TODO list. Status code: {todos_response.status_code}")
                                                                                return

                                                                                todos = todos_response.json()
                                                                                    total_tasks = len(todos)
                                                                                        completed_tasks = sum(1 for todo in todos if todo['completed'])

                                                                                            # Display the progress
                                                                                                print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

                                                                                                    # Display completed tasks
                                                                                                        for todo in todos:
                                                                                                                    if todo['completed']:
                                                                                                                                    print(f"\t {todo['title']}")

                                                                                                                                    if __name__ == "__main__":
                                                                                                                                            if len(sys.argv) != 2:
                                                                                                                                                        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
                                                                                                                                                                sys.exit(1)

                                                                                                                                                                    try:
                                                                                                                                                                                employee_id = int(sys.argv[1])
                                                                                                                                                                                    except ValueError:
                                                                                                                                                                                                print("Error: Employee ID must be an integer.")
                                                                                                                                                                                                        sys.exit(1)

                                                                                                                                                                                                            get_employee_todo_progress(employee_id)
