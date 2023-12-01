class Solution:
    def checkIfPangram(self, A):
        # A = sorted(A)
        # val = 97
        # for i in A:
        #     if ord(i) == val:
        #         val += 1
        # if val == 123:
        #     return True
        # return False
        return len(set(A)) == 26
