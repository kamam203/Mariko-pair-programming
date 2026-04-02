def convert_to_meters(feet, inches):
    """
    Takes two values (feet and inches) and converts them to meters.
    Formula: Total inches * 0.0254
    """
    total_inches = (feet * 12) + inches
    meters = total_inches * 0.0254
    return meters

# Example: 5 feet 10 inches
print(f"5'10'' is {convert_to_meters(5, 10)} meters")
