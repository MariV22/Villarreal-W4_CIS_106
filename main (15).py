def calculate_price_and_tax(quantity):
    # Determine the price based on the quantity
    if quantity > 10000:
        price_per_widget = 10
    elif 5000 <= quantity <= 10000:
        price_per_widget = 20
    else:
        price_per_widget = 30

    # Calculate the extended price
    extended_price = quantity * price_per_widget

    # Calculate the tax amount
    tax_amount = extended_price * 0.07

    # Calculate the total amount
    total_amount = extended_price + tax_amount

    # Display the results
    print(f"Extended Price: ${extended_price:.2f}")
    print(f"Tax Amount: ${tax_amount:.2f}")
    print(f"Total Amount: ${total_amount:.2f}")


# Example usage
quantity = int(input("Enter the quantity of widgets: "))
calculate_price_and_tax(quantity)
