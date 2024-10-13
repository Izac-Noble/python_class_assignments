# def print_welcome(message):
#     print(message)
#     print()
#
# def calculate_miles_per_gallon(miles_driven, gallons):
#     mpg = miles_driven / gallons
#     mpg = round(mpg, 1)
#     return mpg
#
# miles = 500
# gallons = 14
# mpg = calculate_miles_per_gallon(miles,gallons)
# print(mpg)
#
# # if __name__== "main":
# #     main()


TAX_RATE = 0.0
def calc_tax(amount, tax_rate):
    global tax
    tax = amount * TAX_RATE
    return tax

def main():
    tax = calc_tax(85.0, .05)
    print("Tax:", tax)