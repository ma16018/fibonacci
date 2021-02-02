def my_fib(n):
    """Return the n-th Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return my_fib(n-2) + my_fib(n-1)