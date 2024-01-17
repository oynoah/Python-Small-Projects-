def is_leap_year(year):
    """Checks if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def check_leap_years(start_year, end_year):
    leap_years = []
    year_states = {}
    
    for year in range(start_year, end_year + 1):
        is_leap = is_leap_year(year)
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

leap_years_tuple, count_dict = check_leap_years(start_year_range, end_year_range)

print("Year States:")
for year, state in leap_years_tuple:
    print(f"{year}: {state}")

print("\nCount of Leap and Non-Leap Years:")
for state, count in count_dict.items():
    print(f"{state}: {count}")
