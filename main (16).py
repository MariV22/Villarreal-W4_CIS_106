def determine_unit_cost(part_number):
  # Determine the unit cost based on the part number
  if part_number in ["10", "55", 10, 55]:
      return 1.00
  elif part_number in ["99", 99]:
      return 2.00
  elif part_number in ["80", "70", 80, 70]:
      return 3.00
  else:
      return 5.00

def calculate_total_cost(part_number, quantity):
  # Get the unit cost based on the part number
  unit_cost = determine_unit_cost(part_number)

  # Calculate the total cost
  total_cost = quantity * unit_cost

  # Display the results
  print(f"Part Number: {part_number}")
  print(f"Unit Cost: ${unit_cost:.2f}")
  print(f"Total Cost: ${total_cost:.2f}")

# Example usage
part_number = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))
calculate_total_cost(part_number, quantity)