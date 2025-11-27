class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = "" # Initialize to store the longest palindrome
        for i in range(len(s)):
            for j in range(i, len(s)):
                current_substring = s[i:j+1]
                if current_substring == current_substring[::-1]:
                    # If it's a palindrome, check if it's longer than the current longest
                    if len(current_substring) > len(longest_palindrome):
                        longest_palindrome = current_substring
        return longest_palindrome # Return the longest one found