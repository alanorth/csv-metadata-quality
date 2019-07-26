import pandas as pd
import re

def whitespace(field):
    """Fix whitespace issues.

    Return string with leading, trailing, and consecutive whitespace trimmed.
    """


    # Skip fields with missing values
    if pd.isna(field):
        return

    # Initialize an empty list to hold the cleaned values
    values = list()

    # Try to split multi-value field on "||" separator
    for value in field.split('||'):
        # Strip leading and trailing whitespace
        value = value.strip()

        # Replace excessive whitespace (>2) with one space
        pattern = re.compile(r'\s{2,}')
        match = re.findall(pattern, value)

        if len(match) > 0:
            print('DEBUG: Excessive whitespace')
            value = re.sub(pattern, ' ', value)

        # Save cleaned value
        values.append(value)

    # Create a new field consisting of all values joined with "||"
    new_field = '||'.join(values)

    return new_field

