from django.db import models
from django.contrib.auth.models import User


#/orders/ endpoint, primarily requestable through Post request, using those fields (snake_case or CamelCase open to you):
#i. isin (String, 12 chars (this identifies a stock))
# ii. limit_price (Float, always >0)
# iii. side (Enum: buy | sell, case sensitive tolerant)
# iv. valid_until (Integer, Unix UTC Timestamp)
# v. quantity (Integer, always >0)


class Side:
    BUY = 1
    SELL = 2

    CHOICES = (
        (BUY, 'buy'),
        (SELL, 'sell'),
    )


class Orders(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    isin = models.CharField(max_length=12, blank=True)
    limit_price = models.FloatField(null=True,default=0.0)
    side = models.IntegerField(choices=Side.CHOICES)
    valid_until = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField()


