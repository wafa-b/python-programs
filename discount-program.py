amount = float(input("Please Enter the amount "))

discount = 0

final_amount = 0

if amount > 0 and amount < 1000:
    discount = amount * (5/100)
    final_amount = amount-discount
    # print('Your final_amount is  ',final_amount , 'and your discount is ',discount)
elif amount >= 1000 and amount <= 5000:
    discount = amount * (10/100)
    final_amount = amount-discount
    # print('Your final_amount is  ',final_amount , 'and your discount is ',discount)
elif amount > 5000:
    discount = amount * (15/100)
    final_amount = amount-discount
    # print('Your final_amount is  ',final_amount , 'and your discount is ',discount)
else:
    print('Please Enter Correct Number')

print('Your final_amount is  ',final_amount , 'and your discount is ',discount)
