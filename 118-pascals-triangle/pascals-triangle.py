class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev_row = triangle[i-1]
            current_row = [1] # First element of every row is 1
            
            for j in range(1, i):
                # Each element is the sum of the two elements directly above it
                current_row.append(prev_row[j-1] + prev_row[j])
            
            current_row.append(1) # Last element of every row is 1
            triangle.append(current_row)
            
        return triangle