# Programming Assignment 1: Maximum Pairwise Product

# ==============================================================================================================================
# Attempt 1
# ==============================================================================================================================
n = int(input())

while True:
    numbers = list(map(int, input().split()))
# I wanted to make sure the number of numbers in the list is equal to n.
    if len(numbers) != n:
        continue
    else:
        break

max_product = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        product = numbers[i] * numbers[j]

        if product > max_product:
            max_product = product

print(max_product)

# Time complexity: O(n²)
# Result: Time Limit Exceeded.
# case #4/18: time limit exceeded (Time used: 13.99/6.60, memory used: 25088000/536870912.)

# ==============================================================================================================================
# Attempt 2
# ==============================================================================================================================
# My second idea:
# I tried to find the max two numbers without trying every number with a loop inside another loop.
n = int(input())

while True:
    numbers = list(map(int, input().split()))

    if len(numbers) != n:
        continue
    else:
        break

# I created max1 and max2 to keep track of the two largest numbers.
max1 = 0
max2 = 0
# Loop through every number in the list.
for number in numbers:
    # If the current number is bigger than max1,
    # move max1 to max2 and make the current number max1.
    if number > max1:
        max2 = max1
        max1 = number
    # Otherwise, if the number is bigger than max2,
    # make it the new second-largest number.
    elif number > max2:
        max2 = number
# Multiply the two largest numbers to get the maximum product.
print(max1 * max2)

# Time complexity: O(n)
# Result: Accepted.
# Good job! (Max time used: 0.07/6.60, max memory used: 30642176/536870912.)

# ==============================================================================================================================
# What I Learned
# ==============================================================================================================================
#
# My first solution checked every possible pair, which resulted in O(n²) time
# and was too slow for large inputs.
#
# I then realized that I only need the two largest numbers.
# By keeping track of them while looping through the list once,
# I reduced the time complexity to O(n).
#
# Main lesson:
# Look for ways to avoid checking every possible combination.
