""" This script demonstrates a simple sales tax calculation in Python."""

subtotal = 100
sales_tax_rate = 0.0625  # This represents a 6.25% state sales tax rate (commonly used in India)

# Calculate the total by applying the sales tax to the subtotal
total = subtotal * (1 + sales_tax_rate)

print(total)

# print("Debug: calculation complete")  # Debug line temporarily disabled
