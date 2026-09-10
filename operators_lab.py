
# Part 2 — Arithmetic Results
subtotal = 200
discount_rate = 0.10
tax_rate = 0.05

discount_amount = subtotal * discount_rate
price_after_discount = subtotal - discount_amount
tax_amount = price_after_discount * tax_rate
final_price = price_after_discount + tax_amount

print("Discount amount:", discount_amount)
print("Price after discount:", price_after_discount)
print("Tax amount:", tax_amount)
print("Final price:", final_price)

# Part 3 — Division Operators
students = 23
team_size = 5

print("Standard division:", students / team_size)
print("Floor division:", students // team_size)
print("Remainder:", students % team_size)

# Part 4 — Logical Decisions
score = 75
attendance = 0.8

eligible_for_next_topic = score >= 70 and attendance >= 0.75
needs_attention = score < 70 or attendance < 0.75
can_access_course = not needs_attention

print("Eligible for next topic:", eligible_for_next_topic)
print("Needs attention:", needs_attention)
print("Can access course:", can_access_course)
