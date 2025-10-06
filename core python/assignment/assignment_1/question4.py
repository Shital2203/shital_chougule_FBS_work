# Program 4 : Calculates Simple Interest (SI).

if __name__ == "__main__":
    print("\n--- Simple Interest Calculator  ---")
    
    try:
        
        P = float(input("Enter Principal amount (P): "))
        T = float(input("Enter Time in years (T): "))
        R = float(input("Enter Annual Rate of Interest (R, as a percentage): "))
        
        # Calculate Simple Interest
        simple_interest = (P * T * R) / 100
        
        # Display result
        print(f"\nSimple Interest Calculated: {simple_interest:.2f}")
        
    except ValueError:
        print("Error: Please ensure all inputs (P, T, R) are valid numbers.")
