from django.conf.urls import url
from orders.views import CreateOrderView

urlpatterns = [
    url(r"orders/", CreateOrderView.as_view()),
]
