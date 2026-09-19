import random

numbers = [random.uniform(0, 10) for _ in range(5)]

print("Numbers:", numbers)
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
