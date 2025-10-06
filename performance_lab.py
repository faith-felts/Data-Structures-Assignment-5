# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

numbers = [1, 3, 2, 3, 4, 1, 3]

def most_frequent(numbers):
    frequent = {}
    for num in numbers:
        frequent[num] = frequent.get(num, 0) + 1
    return max(frequent, key=frequent.get)

print(most_frequent(numbers))
"""
Time and Space Analysis for problem 1:
- Best-case: O(n)   (we must scan all elements)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)  as in up to n elements; it can be lower if there are duplicates
- Why this approach? 
  Counting frequencies with a dictionary is efficient and easy to read.
- Could it be optimized? 
  Not much; O(n) is optimal since all elements must be seen at least once.

"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]
nums = [4, 5, 4, 6, 5, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

print(remove_duplicates(nums)) 
"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) for the set and result list
- Why this approach?
  Using a set gives O(1) average lookup time while preserving order.
- Could it be optimized?
  Only somwhat; it is already optimal for checking duplicates via the set.



"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]
nums = [1, 2, 3, 4]
target = 5

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

print(find_pairs(nums, target))  
"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach?
  Uses a hash set for O(1) complement lookups and avoids duplicates.
- Could it be optimized?
  A two-pointer approach after sorting is O(n log n); hash set method is better for unsorted lists.


"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    items = []
    if n > 0:
        for i in range(n):
            if size == capacity:
                capacity *= 2
                newList = []
                for j in items:
                    newList.append(j)
                items = newList
                print(f"New capacity = {capacity}")
            items.append(i)
            size += 1
        print(f"Final list size: {size}")
    else:
     print("No items to add")

add_n_items(6)
"""
Time and Space Analysis for problem 4:
- When do resizes happen?
Resizes occur whenever size == capacity (list is full).
- What is the worst-case for a single append?
O(n);  all existing elements must be copied to a new list.
- What is the amortized time per append overall?
O(1) on average; doubling means you do not always have to copy
- Space complexity: O(n)
- Why does doubling reduce the cost overall?
It reduces the frequency of resizing; total copying forms a geometric series,
    then the total cost remains linear across n operations.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

nums = [1, 2, 3, 4]

def running_total(nums):
    result = []
    current_sum = 0
    for num in nums:
        current_sum += num
        result.append(current_sum)
    return result

print(running_total(nums))
"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach?
  Single pass; optimal and easy to understand.
- Could it be optimized?
  possibly slightly, but O(n) time will always be required.

"""

# Optimized Problem #2

def remove_duplicates(nums):
    return list(dict.fromkeys(nums))

print(remove_duplicates([4, 5, 4, 6, 5, 7]))


"""
Time and Space Analysis for problem 2 Optimized:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach?
  dict.fromkeys() removes duplicates and preserves order automatically.
  no need to track seen elements

Comparison to the Original Solution:
- The first solution Used a set() and result list with explicit membership checks inside a loop.
- Optimized version Uses built-in dict.fromkeys(), which handles uniqueness automatically.
- Performance: Both have O(n) time
- Space: Both use O(n) auxiliary space.
"""
