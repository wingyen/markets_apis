from django.db import models
from django.contrib.auth.models import User


class Side(models.TextChoices):
    BUY = "buy", "buy"
    SELL = "sell", "sell"



class Order(models.Model):
    BUY = "buy"
    SELL = "sell"
    SIDE_CHOICES = [
        (BUY, "buy"),
        (BUY, "sell")
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    isin = models.CharField(max_length=12, blank=True)
    limit_price = models.FloatField(null=True,default=0.0)
    side = models.CharField(choices=Side.choices, max_length=4)
    valid_until = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True)




