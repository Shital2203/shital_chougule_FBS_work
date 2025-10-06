# Program 5 : Calculates Compound Interest (CI).

if __name__ == "__main__":

    print("\n--- Annual Compound Interest Calculator  ---")
    
    try:
      
        # P = Principal Amount
        P = float(input("Enter the Principal amount (P): "))
        
        # T = Time in years
        T = float(input("Enter the Time period in years (T): "))
        
        # R = Annual Rate of Interest (as a percentage)
        R = float(input("Enter the Annual Rate of Interest (R, as a percentage): "))
        
        # Convert rate percentage to decimal 
        rate_decimal = R / 100.0
        
        # Calculate Total Amount (A) using the built-in ** operator for exponentiation
        # Formula: A = P * (1 + R)^T
        amount = P * ((1 + rate_decimal) ** T)
        
        # Calculate Compound Interest (CI)
        # CI = A - P
        compound_interest = amount - P

        # Display results
        print("\n--- Results ---")
        print(f"Total Amount (A): ${amount:.2f}")
        print(f"Compound Interest (CI): ${compound_interest:.2f}")
        
    except ValueError:
        print("Error: Please ensure all inputs (P, T, R) are valid numbers.")
    except Exception as e:
        # Catch unexpected errors, which are less likely without the math module, 
        # but good practice for robust code.
        print(f"An unexpected error occurred: {e}")
