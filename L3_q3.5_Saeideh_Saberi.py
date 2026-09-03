'''
session-03 

q3.5

--------product----Discount----

'''

#q3.5.1
#q3.5.2

product = input('name of the product:')
price = float(input('set the price:'))
discount = str(input('discount code is:'))

if discount.lower().strip() == 'z14':
        newprice = price - (price * 20/100)
        print('new price is:', newprice)
else: 
        print('discount code is not correct')
        
        
        
#q3.5.3

product1 = input('name of the product1:')
price1 = float(input('set the price1:'))
discount1 = str(input('discount1 code is:'))

if discount1.lower().strip() != 'z14':
        print('discount code is not correct')
        discount1 = str(input('enter discount1 code one more time:'))
        if discount1.lower().strip() == 'z14':
                newprice2 = price1 - (price1 * 20/100)
                print('new price is:', newprice2)
        else: 
                print('you are BLOKED')