def convert_temp(input_scale,output_scale,value):
    """Converts temperature from one scale to another.
                - Celsius
                - Kelvin
                - Fahrenheit

    Args:
        input_scale (str): The temperature scale of the input value.
        output_scale (str): The temperature scale to which the input value is to be converted.
        value (float): The temperature value to be converted.

    Returns:
        float: The converted temperature value.

    Raises:
        ValueError: If the input/output temperature scale is invalid.
    """
    while value != None and input_scale != None and output_scale != None:
        if input_scale == 'Celsius':
            if output_scale == 'Fahrenheit':
                return value * (9/5) + 32
            elif output_scale == 'Kelvin':
                return value + 273.15
        elif input_scale == 'Fahrenheit':
            if output_scale == 'Celsius':
                return (value-32) * (5/9)
            elif output_scale == 'Kelvin':
                return (value + 459.67) * (5/9)
        elif input_scale == 'Kelvin':
            if output_scale == 'Celsius':
                return value - 273.15
            elif output_scale == 'Fahrenheit':
                return (value * (9/5)) - 459.67
        else:
            raise ValueError('ERROR: Invalid input/output temperature scale.')


# Example usage
if __name__ == "__main__":
    converted_value = convert_temp(value=0, input_scale='Celsius', output_scale='Kelvin')
    print(f"Converted Value is equal to {converted_value}")
