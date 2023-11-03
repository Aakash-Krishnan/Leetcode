class Solution:
    def isPalindrome(self, A: str) -> bool:
        word=""

        for i in A.lower():
            if i.isalnum():
                word += i
        def recursion(A, i, j):
            if i >= j:
                return True

            if A[i] == A[j]:
                return recursion(A, i+1, j-1)
            else:
                return False

        return recursion(word, 0, len(word)-1)