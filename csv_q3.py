#!/usr/bin/python3
"""This script reads a CSV file of employees, counts how many
in the department and generates a report with the information in plain text"""

import csv

def read_employees(csv_file_location):
    """Receives a CSV file as a parameter and returns a list of dictionaries"""

    with open(csv_file_location) as employee_file:
        # add a dialect for flexibility during parsing
        csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
        reader = csv.DictReader(employee_file, dialect="empDialect")
        employee_list = []
        for data in reader:
            employee_list.append(data)

    return employee_list

def process_data(employee_list):
    """Receives a list of dictionaries and returns a dictionary with number
    of staff in each department"""

    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data["Department"])

    department_data = {}
    # set is used to get unique values for department_name
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data

def write_report(dictionary, report_file):
    """Writes the dictionary containing number of staff to a plain text file"""

    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ":" + str(dictionary[k] + "\n"))
        f.close()

# Test functions. Change parameters as needed
employee_list = read_employees("/home/umjoji/Github/IT_Automation_with_Python/employees.csv")
print(employee_list)
dictionary = process_data(employee_list)
print(dictionary)
write_report(dictionary, "report.txt")
