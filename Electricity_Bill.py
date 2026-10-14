
def calculateHomeCharges(a, b):
    amount = a + b
    tax = amount * 5 / 100
    return amount + tax


def calculateCoolingCharges(c, d):
    amount = c + d
    tax = amount * 10 / 100
    return amount + tax


def calculateLightingCharges(e):
    tax = e * 8 / 100
    return e + tax


def totalBill(a, b, c, d, e):
    home = calculateHomeCharges(a, b)
    cooling = calculateCoolingCharges(c, d)
    lighting = calculateLightingCharges(e)

    return home + cooling + lighting


def calculateFinalBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 10 / 100
    return total - discount


# Sample values
a = 100
b = 100
c = 100
d = 100
e = 100

# Calculations
total = totalBill(a, b, c, d, e)
final_amount = calculateFinalBill(a, b, c, d, e)
discount = total * 10 / 100

# Display output
print(f"Home charges = Rs. {calculateHomeCharges(a, b):.2f}")
print(f"Cooling charges = Rs. {calculateCoolingCharges(c, d):.2f}")
print(f"Lighting charges = Rs. {calculateLightingCharges(e):.2f}")
print(f"Total after tax = Rs. {total:.2f}")
print(f"Discount = Rs. {discount:.2f}")
print(f"Final electricity bill = Rs. {final_amount:.2f}")
