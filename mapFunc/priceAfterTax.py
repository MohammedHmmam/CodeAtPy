#Consider  situation in which you need to calculate
#the price after Tax for a list of Transactions:
txns = [1.09 , 23.56 , 57.84 , 4.56 , 6.78]
TAX_RATE = 0.08
def get_price_with_tax(txn):
    return txn * (1+TAX_RATE)

final_prices = map(get_price_with_tax , txns)
print(list(final_prices))    