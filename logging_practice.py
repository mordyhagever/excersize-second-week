
import logging
#tar1

logging.basicConfig(
    filename="shop.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)%"
)
logging.info("order 17 created")
logging.warning("low stock: only two left")

#tar3

def loggings():
    sum_payment = 0
    payments = ["120", "abc", "80"]
    for pay in payments:
        try:
            sum_payment += int(pay)
        except ValueError:
            logging.error("string is not a number")
    return f"Total charges: {sum_payment}"
print(loggings())



