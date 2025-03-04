class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_count = {}  # Dictionary to store prefix sums
        prefix_count[0] = 1  # Base case: sum=0 occurs once
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num  # Update prefix sum

            # Check if (current_sum - k) exists in dictionary
            if (current_sum - k) in prefix_count:
                count += prefix_count[current_sum - k]  # Add occurrences

            # Store/update prefix sum count
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1  

        return count