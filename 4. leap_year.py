def isLeapYear(year):
    """
    Check if a given year is a leap year.

    Parameters:
    - year (int): The year to be checked.

    Returns:
    - bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def checkLeapYearsInRange(start_year, end_year):
    """
    Check leap years in a given range and store their states in a tuple.
    Count the instances and store in a dictionary.

    Parameters:
    - start_year (int): The start year of the range.
    - end_year (int): The end year of the range.

    Returns:
    - tuple: A tuple containing the leap year states.
    - dict: A dictionary containing the count of leap and non-leap years.
    """
    leap_years = []
    year_states = {}

    for year in range(start_year, end_year + 1):
        is_leap = isLeapYear(year)
        leap_years.append((year, is_leap))

        if is_leap:
            year_states[year] = 'Leap Year'
        else:
            year_states[year] = 'Non-Leap Year'

    leap_year_count = sum(
        1 for state in year_states.values() if state == 'Leap Year')
    non_leap_year_count = sum(
        1 for state in year_states.values() if state == 'Non-Leap Year')

    count_dict = {'Leap Year': leap_year_count,
                  'Non-Leap Year': non_leap_year_count}

    return tuple(leap_years), count_dict


# Example usage:
start_year_range = 1900
end_year_range = 2000

leap_years_tuple, count_dict = checkLeapYearsInRange(
    start_year_range, end_year_range)

print("Year States:")
for year, state in leap_years_tuple:
    print(f"{year}: {state}")

print("\nCount of Leap and Non-Leap Years:")
for state, count in count_dict.items():
    print(f"{state}: {count}")
