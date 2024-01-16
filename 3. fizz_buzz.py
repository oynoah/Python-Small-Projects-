def fizz_buzz(number):
    output_list = ()
    
    counts = {'Fizz': 0, 'Buzz': 0, 'FizzBuzz': 0, 'Number': 0}

    # Loop through numbers from 1 to the input number
    for num in range(1, number+1):
        
        if num % 3 == 0 and num % 5 == 0:
            output_list += ('FizzBuzz',)  
            counts['FizzBuzz'] += 1  
        
        elif num % 3 == 0:
            output_list += ('Fizz',)  
            counts['Fizz'] += 1  
        
        elif num % 5 == 0:
            output_list += ('Buzz',)  
            counts['Buzz'] += 1 
        
        else:
            output_list += (num,)  
            counts['Number'] += 1  

    return output_list, counts


# Call the function and store the results in two variables
output, count_results = fizz_buzz(100)

# Display the output list and the counts dictionary
print("Output List:", output)
print("Counts Dictionary:", count_results)
