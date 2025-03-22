class Solution(object):
    def spiralOrder(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        left=0
        right=m-1
        top=0
        bottom=n-1
        result=[]
        count=0
        while count <= m*n:
            if count >= m*n:
                break
            for j in range(left,right+1):
                result.append(matrix[top][j])
                count +=1
            top +=1
            if count >= m*n:
                break
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
                count +=1
            right -=1
            if count >= m*n:
                break
            for j in range(right,left-1,-1):
                result.append(matrix[bottom][j])
                count+=1
            bottom -=1
            if count >= m*n:
                break
            for i in range(bottom,top,-1):
                result.append(matrix[i][left])
                count +=1
            left +=1
        return matrix
            


# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sol = Solution()
    print(sol.spiralOrder(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]