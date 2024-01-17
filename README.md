# Python Small Projects


## 1. Temperature Converter

### Functionality
- Supports conversion between all three scales(Celsius, Fahrenheit & Kelvin).

- Accepts user-defined input and output scales.

- Returns the converted temperature value as a float.

## 2. Odd Even Evaluation

### Functionality

- The program first checks if a number is less than 0, which would make it negative. If so, it sets the variable `number_type` to “Negative”. Otherwise, `number_type` is set to “Positive”.

- Next, the program checks if `number` is divisible by 2 with no remainder, using the modulo operator `%`.
  
- If the result is 0, the number is even, and the function returns the string "`{number_type} Even`". If there is a remainder, the number is odd, and the function returns "`{number_type} Odd`".

## 3. FizzBuzz 

### Functionality

- The program first initializes an empty tuple list called `output_list` to store the output for each result. It initilizes a dictionary called `counts` to track counts of different categories ('Fizz,' 'Buzz,' 'FizzBuzz,' and 'Number').

- Next, the program takes the number input and iterates through it to find instances where the condition for the `FizzBuzz` fits. 

- Returns a tuple containing `output_list` and the `counts` dictionary.

## 4. Leap Years

### Functionality
- The program starts with a helper function to check if a year is a leap year or not

- The following function iterates through a range of years given as argument an then counts each instance of leap and not leap year and stores them in a dictionary. 

- Returns a tuple containing the leap year information and the count dictionary.


