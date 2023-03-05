import random

lotto_numbers = []

while len(lotto_numbers) < 6:
    lotto_numbers.append(random.randint(0,51))
print(lotto_numbers)


