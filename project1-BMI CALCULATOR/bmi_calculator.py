
#   BMI Calculator - Python (Beginner Level)
 


def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def get_valid_input(prompt, min_val, max_val):
    """Prompt user for a valid number within a given range."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  ⚠  Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  ⚠  Invalid input. Please enter a number.")

def main():
    print("=" * 40)
    print("        BMI CALCULATOR")
    print("=" * 40)

    # Get user inputs
    weight = get_valid_input("Enter your weight (kg): ", 1, 500)
    height = get_valid_input("Enter your height (m):  ", 0.5, 3.0)

    # Calculate and classify
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    # Display results
    print()
    print("-" * 40)
    print(f"  Your BMI      : {bmi:.2f}")
    print(f"  Category      : {category}")
    print("-" * 40)
    print()
    print("  BMI Categories:")
    print("  < 18.5    →  Underweight")
    print("  18.5–24.9 →  Normal weight")
    print("  25.0–29.9 →  Overweight")
    print("  ≥ 30.0    →  Obese")
    print("=" * 40)

if __name__ == "__main__":
    main()
