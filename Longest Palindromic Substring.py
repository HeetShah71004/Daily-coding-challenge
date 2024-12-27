def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    result = ""
    for i in range(len(s)):
        # Odd length palindrome
        temp = expand_around_center(i, i)
        if len(temp) > len(result):
            result = temp
        
        # Even length palindrome
        temp = expand_around_center(i, i+1)
        if len(temp) > len(result):
            result = temp

    return result

# Example
print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"
