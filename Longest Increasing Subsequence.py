def longest_increasing_subsequence(nums):
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example
print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
