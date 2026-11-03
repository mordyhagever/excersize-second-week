# from excersize_second_week.Modules.prices import add_vat
# from Modules import  prices
import Modules.prices
# from excersize_second_week.Modules import prices




discount = Modules.prices.apply_discount(200, 10)
with_vat = discount + Modules.prices.add_vat(discount)
print(discount)
print(with_vat)


#tar2
#see first lines in file

#tar3
