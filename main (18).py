def determine_ticket_price(quantity):
  # Determine the price per ticket based on the quantity
  if quantity >= 25:
      return 50
  elif 10 <= quantity <= 24:
      return 60
  elif 5 <= quantity <= 9:
      return 70
  else:
      return 75

def calculate_total_cost(quantity):
  # Get the price per ticket based on the quantity
  price_per_ticket = determine_ticket_price(quantity)

  # Calculate the total cost
  total_cost = quantity * price_per_ticket

  # Display the results
  print(f"Number of Tickets: {quantity}")
  print(f"Price Per Ticket: ${price_per_ticket:.2f}")
  print(f"Total Cost: ${total_cost:.2f}")

# Example usage
quantity = int(input("Enter the number of concert tickets: "))
calculate_total_cost(quantity)