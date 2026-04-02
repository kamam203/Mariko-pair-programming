# FEEDBACK FOR PARTNER:
# 1. The mathematical logic for x = r*cos(theta) and y = r*sin(theta) is correct.
# 2. The function is well-structured and uses the math library properly.
# 3. Suggestion: You could add a check to make sure the radius 'r' is not negative.

import math

def polar_to_cartesian(radius, angle_radians):
    """Converts polar coordinates (r, theta) to Cartesian (x, y)."""
    x = radius * math.cos(angle_radians)
    y = radius * math.sin(angle_radians)
    return x, y
