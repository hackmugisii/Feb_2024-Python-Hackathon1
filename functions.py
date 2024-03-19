def fibonacci(n):
   
    sequence = [0, 1]  # Initialize the first two terms
    
    # Generate the remaining terms
    for i in range(2, n):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)
    
    return sequence[:n]  # Return the sequence up to the nth term


n = int(input("Enter the number of terms: "))

fib_sequence = fibonacci(n)

print(f"The Fibonacci sequence up to the {n}th term is: {fib_sequence}")
