class Solution:
    def painting_problem(A, B, X, Y):
        return 2 * max((A + B) * max(X, Y), (X + Y) * max(A + B))
print(Solution.painting_problem(2, 2, 4, 4))