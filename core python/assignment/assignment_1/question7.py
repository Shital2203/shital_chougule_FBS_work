# Program 7 : Finds the roots of a quadratic equation.
import math

if __name__ == "__main__":
    print("\n--- Quadratic Equation Root Finder (ax^2 + bx + c = 0) ---")
    
    try:
        # Get the coefficients a, b, and c
        a = float(input("Enter coefficient 'a': "))
        b = float(input("Enter coefficient 'b': "))
        c = float(input("Enter coefficient 'c': "))
        
        # Check if it's actually a quadratic equation (a cannot be 0)
        if a == 0:
            print("Error: The coefficient 'a' cannot be zero for a quadratic equation.")
        else:
            # 1. Calculate the Discriminant (Delta)
            # Delta = b^2 - 4ac
            discriminant = (b**2) - (4 * a * c)
            
            # The nature of the roots depends on the discriminant:

            if discriminant > 0:
                # Case 1: Two distinct real roots
                root1 = (-b + math.sqrt(discriminant)) / (2 * a)
                root2 = (-b - math.sqrt(discriminant)) / (2 * a)
                
                print("\nResult: Two distinct real roots.")
                print(f"Root 1 (x1): {root1:.4f}")
                print(f"Root 2 (x2): {root2:.4f}")
                
            elif discriminant == 0:
                # Case 2: One real root (two equal roots)
                root = -b / (2 * a)
                
                print("\nResult: One real root (equal roots).")
                print(f"Root (x): {root:.4f}")
                
            else: # discriminant < 0
                # Case 3: Two complex roots
                # We split the formula: x = (-b / 2a) +/- (sqrt(|Delta|) / 2a) * i
                real_part = -b / (2 * a)
                imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
                
                print("\nResult: Two complex roots.")
                print(f"Root 1 (x1): {real_part:.4f} + {imaginary_part:.4f}i")
                print(f"Root 2 (x2): {real_part:.4f} - {imaginary_part:.4f}i")

    except ValueError:
        print("Error: Please enter valid numbers for the coefficients (a, b, c).")
