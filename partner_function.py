import math

def polar_to_cartesian(radius, angle_radians):
    """Converts polar coordinates (r, theta) to Cartesian (x, y)."""
    x = radius * math.cos(angle_radians)
    y = radius * math.sin(angle_radians)
    return x, y