import timeit
import random

setup = """
import random
a = random.randint(1, 100)
b = random.randint(1, 100)
"""

# Case 1: always create full list
test_full = """
ops = [a*b, a+b, a-b, b-a, a//b if b else 0, b//a if a else 0]
"""

# Case 2: create base list, then conditionally add
test_conditional = """
ops = [a*b, a+b, a-b, b-a]
if b != 0 and a % b == 0:
    ops.append(a//b)
if a != 0 and b % a == 0:
    ops.append(b//a)
"""

iterations = 1_000_000

time_full = timeit.timeit(test_full, setup=setup, number=iterations)
time_conditional = timeit.timeit(test_conditional, setup=setup, number=iterations)

print(f"Full list time:        {time_full:.4f} seconds")
print(f"Conditional list time: {time_conditional:.4f} seconds")
