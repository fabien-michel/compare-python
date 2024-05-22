import sys
import timeit
def test_function():
    numbers = list(range(1000))
    [num ** 2 for num in numbers]

# Use timeit to benchmark the function
benchmark_result = timeit.timeit(test_function, number=int(sys.argv[1]) )

print(benchmark_result)