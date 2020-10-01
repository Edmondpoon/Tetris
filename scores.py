def score_change(level, rows_cleared, points):
    point_system = {1 : 40 * (level + 1), 2 : 100 * (level + 1), 3 : 300 * (level + 1), 4 : 1200 * (level + 1), None : 0}
    return points + point_system[rows_cleared]
