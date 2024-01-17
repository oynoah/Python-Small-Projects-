def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def evaluate_numbers(numbers):
    prime_not_prime_tuple = ()
    counts = {'prime': 0, 'not_prime': 0}

    for num in numbers:
        if is_prime(num):
            prime_not_prime_tuple += ('prime',)
            counts['prime'] += 1
        else:
            prime_not_prime_tuple += ('not_prime',)
            counts['not_prime'] += 1

    return prime_not_prime_tuple, counts


# Example usage:
input_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
result_tuple, count_dict = evaluate_numbers(input_numbers)

print(f"Results Tuple: {result_tuple}")
print(f"Counts Dictionary: {count_dict}")
