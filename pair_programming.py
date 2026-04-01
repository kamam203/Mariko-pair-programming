def convert_to_meters(feet, inches):
    """
    Takes two values (feet and inches) and converts them to meters.
    1 foot = 0.3048 meters, 1 inch = 0.0254 meters.
    """
    meters = (feet * 0.3048) + (inches * 0.0254)
    return meters

print(f"5 feet 10 inches is {convert_to_meters(5, 10)} meters")