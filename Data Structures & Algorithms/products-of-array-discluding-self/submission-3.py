class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 🧠 IDEA:
        # For each index, the result should be:
        # product of all elements to the LEFT of it
        # multiplied by
        # product of all elements to the RIGHT of it.
        #
        # We do this in two passes:
        # 1. Left to right → store prefix products
        # 2. Right to left → multiply postfix products
        #
        # This avoids division and works in O(n) time.

        # ⏱️ Time Complexity:
        # O(n) → two linear passes

        # 🧠 Space Complexity:
        # O(1) extra space (output array not counted)

        # Result array initialized with 1s
        res = [1] * len(nums)

        # First pass: prefix product
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix          # product of elements before i
            prefix = prefix * nums[i]

        # Second pass: postfix product
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * postfix  # multiply with product of elements after i
            postfix = postfix * nums[i]

        return res
