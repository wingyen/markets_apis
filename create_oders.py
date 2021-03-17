from flask import Flask


app = Flask(__name__, static_host="https://api.lemon.markets/rest/v1/", host_matching=True)




#/orders/ endpoint, primarily requestable through Post request, using those fields (snake_case or CamelCase open to you):
#i. isin (String, 12 chars (this identifies a stock))
# ii. limit_price (Float, always >0)
# iii. side (Enum: buy | sell, case sensitive tolerant)
# iv. valid_until (Integer, Unix UTC Timestamp)
# v. quantity (Integer, always >0)



def create_order():
    pass


