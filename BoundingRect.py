# Keep Coding And change the world and do not forget anything... Not Again..
def bounding_rect(white, i, j, l, r):
    a, b, c, d = i, j, i, j
    stack = {(i, j)}

    # Performing flood fill to identify complete block
    cl = white[i][j]
    while stack:
        i, j = stack.pop()
        a, b, c, d = min(i, a), min(j, b), max(i, c), max(j, d)
        white[i][j] = -1
        if i > 0 and white[i - 1][j] == cl:
            stack.add((i - 1, j))
        if j > 0 and white[i][j - 1] == cl:
            stack.add((i, j - 1))
        if i < l - 1 and white[i + 1][j] == cl:
            stack.add((i + 1, j))
        if j < r - 1 and white[i][j + 1] == cl:
            stack.add((i, j + 1))

    return white, a, b, c, d
