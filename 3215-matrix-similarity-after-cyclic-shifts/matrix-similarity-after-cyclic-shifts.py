class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k = k % n
        for i in range(m):
            shifted = mat[i][-k:] + mat[i][:-k] if i & 1 else mat[i][k:] + mat[i][:k]
            if shifted != mat[i]:
                return False
        return True

