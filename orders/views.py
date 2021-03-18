from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta


from orders.models import Order, Side


class OrderSerializer(serializers.ModelSerializer):
    isin = serializers.CharField(required=True)
    limit_price = serializers.FloatField
    side = serializers.ChoiceField(choices=Side)
    valid_until = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = Order
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
        # now = datetime.now()
        # days = self.request.data['valid_until']
        side = self.request.data["side"].lower()
        valid_until = int(self.request.data["valid_until"])
        quantity = abs(self.request.data['quantity'])
        order = Order.objects.create(
            user=user,
            isin=isin,
            limit_price=limit_price,
            side=side,
            valid_until=valid_until,
            quantity=quantity,
        )

        return order

