def determine_interest_rate(principal, years_to_maturity):
  # Determine the interest rate based on the principal and years to maturity
  if principal > 100000 and years_to_maturity == 5:
      return 0.06
  elif 50000 <= principal <= 100000 and years_to_maturity == 10:
      return 0.05
  elif 50000 <= principal <= 100000 and years_to_maturity == 5:
      return 0.04
  else:
      return 0.02

def calculate_first_year_interest(principal, years_to_maturity):
  # Get the interest rate based on the principal and years to maturity
  interest_rate = determine_interest_rate(principal, years_to_maturity)

  # Calculate the first-year interest
  interest_amount = principal * interest_rate

  # Display the results
  print(f"Principal: ${principal:.2f}")
  print(f"Interest Rate: {interest_rate * 100:.2f}%")
  print(f"First Year Interest Amount: ${interest_amount:.2f}")

# Example usage
principal = float(input("Enter the principal amount of the CD: "))
years_to_maturity = int(input("Enter the years to maturity of the CD: "))
calculate_first_year_interest(principal, years_to_maturity)