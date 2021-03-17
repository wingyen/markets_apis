from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from datetime import datetime, timedelta

from orders.models import Orders, Side


class OrderSerializer(serializers.ModelSerializer):
    isin = serializers.CharField(required=True)
    limit_price = serializers.FloatField
    side = serializers.ChoiceField(required=True, choices=Side.CHOICES)
    valid_until = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = Orders
        fields = [
            "isin",
            "limit_price",
            "side",
            "valid_until",
            "quantity"
        ]




class CreateOrderView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user = self.request.user
        isin = self.request.data['isin'].upper()  # all letters should be upper case
        limit_price = abs(self.request.data['limit_price'])  # always > 0
        now = datetime.now()
        days = self.request.data['valid_until']  # future days
        valid_until = int(datetime.timestamp(now + timedelta(days=days)))
        quantity = abs(self.request.data['quantity'])
        order = Orders.objects.create(
            user=user,
            isin=isin,
            limit_price=limit_price,
            valid_until=valid_until,
            quantity=quantity,
        )
        order.save()



