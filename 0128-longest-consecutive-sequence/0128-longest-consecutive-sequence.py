class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        longest = 0

        for x in num_set:

            if x-1 not in num_set:
                
                length = 1
                current = x

                while current+1 in num_set:

                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


        