class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D array (m rows, n columns) with all ones
        # Each cell (i, j) will store the number of unique paths to reach that cell
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # For cells other than the first row and first column,
        # the number of paths to reach them is the sum of paths from the cell above
        # and the cell to the left.
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The result is the number of paths to the bottom-right corner (m-1, n-1)
        return dp[m-1][n-1]