import re

def validate_date_format(date_string):
    # Define the regular expression pattern for the date format YYYY-MM-DD
    pattern = r'^202[4]-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
    
    # Use the re.match function to check if the string matches the pattern
    if re.match(pattern, date_string):
        return True
    else:
        return False
    
def dynamic_type(dynamic):
    if validate_date_format(dynamic):
        return 'date'
    
    # elif

    else:
        return None
