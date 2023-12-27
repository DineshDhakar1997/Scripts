# split_function.py

import re

def split_by_special_chars(input_string):
    # Define a regular expression pattern to match any non-alphanumeric character
    pattern = re.compile(r'\W+')

    # Split the string using the regular expression pattern
    result_list = re.split(pattern, input_string)

    # Remove empty strings from the result list
    result_list = list(filter(None, result_list))

    return result_list
