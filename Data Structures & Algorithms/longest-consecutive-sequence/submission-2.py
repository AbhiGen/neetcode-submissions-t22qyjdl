class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 🧠 IDEA:
        # We want to find the longest sequence of consecutive numbers.
        #
        # Convert the list into a set for O(1) lookups.
        # Only start counting when we find the START of a sequence.
        # A number is the start if (number - 1) is NOT in the set.
        #
        # From that starting number, keep checking the next consecutive
        # numbers until the sequence breaks.

        # ⏱️ Time Complexity:
        # O(n) → each number is visited at most twice

        # 🧠 Space Complexity:
        # O(n) → for storing numbers in a set

        numSet = set(nums)  # Store all numbers for fast lookup
        longest = 0        # Stores the length of the longest sequence

        for n in numSet:
            # Check if n is the start of a sequence
            if n - 1 not in numSet:
                length = 1  # Current sequence length

                # Count consecutive numbers starting from n
                while n + length in numSet:
                    length += 1

                # Update longest sequence found
                longest = max(longest, length)

        return longest
