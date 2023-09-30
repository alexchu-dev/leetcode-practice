class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Parameters: An integer.
        Returns: True if palindrome else False.
        Exception: If string is inserted.
        """
        def recursive_isPalindrome(input, left, right):
            if left >= right:
                return True
            else:
                if input[left] != input[right]:
                    return False
                else:
                    return recursive_isPalindrome(input, left + 1, right - 1)
        if x < 0 :
            return False
        return recursive_isPalindrome(str(x), 0, len(str(x)) - 1)

y = Solution()
print(y.isPalindrome(121))