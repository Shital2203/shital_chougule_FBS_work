# Program 3: Finds the quotient and remainder of two integer numbers.

def find_quotient_remainder():

    print("\n--- Quotient and Remainder Finder ---")
    try:
        dividend = int(input("Enter the dividend (the number being divided): "))
        divisor = int(input("Enter the divisor (the number dividing): "))
        
        if divisor == 0:
            print("Error: The divisor cannot be zero (Division by zero is undefined).")
            return

        # Quotient (// performs integer division)
        quotient = dividend // divisor
        
        # Remainder (% performs modulo operation)
        remainder = dividend % divisor  
        
        print(f"\nDividend: {dividend}")
        print(f"Divisor: {divisor}")
        print("-" * 30)
        print(f"Quotient (Q): {quotient}")
        print(f"Remainder (R): {remainder}")
        
    except ValueError:
        print("Error: Invalid input. Please enter whole numbers (integers).")

if __name__ == "__main__":
    find_quotient_remainder()
