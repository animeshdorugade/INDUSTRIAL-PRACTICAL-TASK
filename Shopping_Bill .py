
def calculateElectronicsGST(a, b):
    amount = a + b
    return amount + (amount * 18 / 100)


def calculateFashionGST(c, d):
    amount = c + d
    return amount + (amount * 13 / 100)


def calculateFoodGST(e):
    return e + (e * 7 / 100)


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


# Main method call with sample values
a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print(f"Total after GST = Rs. {total:.2f}")
print(f"Discount = Rs. {discount:.2f}")
print(f"Final payable amount = Rs. {final_amount:.2f}")
