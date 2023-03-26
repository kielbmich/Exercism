def saddle_points(matrix):
    if not matrix:
        return []
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    if not all(len(row) == n_cols for row in matrix):
       raise ValueError("irregular matrix")
    out = []
    for i in range(n_rows):
        for j in range(n_cols):
            if all([matrix[i][j] >= item for item in matrix[i]]) and all([matrix[i][j] <= item for item in list(zip(*matrix))[j]]):
                out.append({"row": i + 1, "column": j + 1})
    return out