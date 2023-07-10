#!/usr/bin/env python3

import csv
import re

# two dictionaries for:
# error messages
# count number of user entries between INFO and ERROR
errors = {}
user_entries = {}

# parse through logfile
with open('syslog.logs') as my_file:
    for line in my_file:
        username = re.search(r"\((.*)\)", line).group(1)
        user_count = {'INFO': 0, 'ERROR': 0}
        if username not in user_entries:
            user_entries[username] = user_count
        # For each log entry, first check if it matches the INFO or ERROR message
        # You should use regular expressions for this.
		# When you get a successful match,
        # add one to the corresponding value in the user_entries dictionary.
        if 'INFO' in line:
            user_entries[username]['INFO'] += 1
        # If you get an ERROR message, add one to the corresponding entry
        # in the error dictionary by using proper data structure.
        elif 'ERROR' in line:
            error_msg = re.search(r'ERROR (.*) ', line).group(1)
            if error_msg not in errors:
                errors[error_msg] = 0
            errors[error_msg] += 1
            user_entries[username]['ERROR'] += 1
        else:
            pass

# lists to sort errors and user_entries
error_sorted = []
user_sorted = []

# sort error messages by number of occurrences
for error, count in sorted(errors.items(), key=lambda item: item[1], reverse=True):
    error_sorted.append([error, count])

# sort user_entries by number of occurrences of username
for username in sorted(user_entries.keys()):
    user_sorted.append([username, user_entries[username]['INFO'], user_entries[username]['ERROR']])

# insert column names for both
error_sorted.insert(0, ["Error", "Count"])
user_sorted.insert(0, ["Username", "INFO", "ERROR"])

# store error messages in csv file
with open('error_message.csv', 'w') as error_msg_file:
    writer = csv.writer(error_msg_file)
    writer.writerows(error_sorted)
    error_msg_file.close()

# store user entries in csv file
with open('user_statistics.csv', 'w') as user_statistics_file:
    writer = csv.writer(user_statistics_file)
    writer.writerows(user_sorted)
    user_statistics_file.close()
