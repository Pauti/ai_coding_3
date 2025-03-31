def fibonacci(n, memo={}):
    """
    Calculate the nth Fibonacci number using an iterative approach with memoization.
    
    Args:
        n (int): The position in the Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result

# Example usage
print(fibonacci(10))

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of the number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial: " + str(factorial(5)))
