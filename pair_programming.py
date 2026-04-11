def convert_to_meters(feet, inches):
    """
    Takes two values (feet and inches) and converts them to meters.
    Formula: Total inches * 0.0254
    """

# CODE REVIEW:
# - Looks good! Excellent use of a docstring to explain the math, and the logic is really good!.
# - Could be improved: You could add a quick check to handle negative inputs or ensure 'feet' and 'inches' are numeric types.

    total_inches = (feet * 12) + inches
    meters = total_inches * 0.0254
    return meters

# Example: 5 feet 10 inches
print(f"5'10'' is {convert_to_meters(5, 10)} meters")
