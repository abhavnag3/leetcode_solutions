class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result
'''class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        subFromRowT = 0
        subFromColT = 0
        
        #index, value
        visitedDict = {}
        r1 = 0
        c1 = len(matrix[0])
        
        while len(visitedDict.keys()) != (len(matrix) * len(matrix[0])):
            
            returnRow(matrix, r1, visitedDict)
            returnColumn(matrix, c1, visitedDict)
            returnRowRev(matirx, rr, visitedDict)
            returnColRev(matrix, cr, visitedDict)
            
            r1 += 1
            c1 -= 1
            rr -= 1
            cr += 1
        
        
    
    def returnColumn(matrix, columnNum, visitedDict):
        res = []
        for i in range(len(matrix)):
            if (i + columnN) in visitedDict.keys():
                continue
            else:
                visitedDict[i + columnN] = matrix[i][columnNum]
                res.append(matrix[i][columnNum])
        
        return visitedDict, res    
                
                
    
    def returnRow(matrix, rowNum, visitedDict):
        res = []
        for i in range(len(matrix[0])):
            if (i + rowNum) in visitedDict.keys():
                continue
            else:
                visitedDict[i + rowNum] = matrix[rowNum][i]
                res.append(matrix[rowNum][i])
        return visitedDict, res'''
        