'''
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?
'''

cover_price = 24.95
discount = 40
shipping_first_copy = 3
shipping_rest_copies = 0.75

wholesale_cost = (0.6 * 24.95 * 60) + (3 + 59*0.75)
print("The total wholesale cost is", wholesale_cost)
