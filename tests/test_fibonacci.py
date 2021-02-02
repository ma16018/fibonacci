from my_fibonacci import my_fib

def test_fibonacci_values():

    for i, f in enumerate([1, 1, 2, 3, 5, 8]):
        assert my_fib(i+1) == f