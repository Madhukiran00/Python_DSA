l=[[1,2,3],
   [4,5,6],
   [7,8,9]]

def matrix(l):
    result = []
    if not l:
        return result

    top = 0
    bottom = len(l) - 1
    left = 0
    right = len(l[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from Left to Right (Top Row)
        for col in range(left, right + 1):
            result.append(l[top][col])
        top += 1

        # Traverse from Top to Bottom (Right Column)
        for row in range(top, bottom + 1):
            result.append([row][right])
        right -= 1

        # Traverse from Right to Left (Bottom Row)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append([bottom][col])
            bottom -= 1

        # Traverse from Bottom to Top (Left Column)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append([row][left])
            left += 1

    return result

print(matrix(l))
        