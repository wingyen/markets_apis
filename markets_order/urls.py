from django.contrib import admin
from django.urls import path, include

from users.views import UserView, UserDetail
from rest_framework.authtoken import views

from rest_framework_swagger.views import get_swagger_view



urlpatterns = [
    path("", include("users.urls")),
    path('admin/', admin.site.urls),
    path('api/users/', UserView.as_view()),
    path('api/users/<int:pk>/', UserDetail.as_view()),
    path('api/token/', views.obtain_auth_token),
    path('api/accounts/', include("orders.urls")),

]
schema_view = get_swagger_view(title="Markets API", patterns=urlpatterns,)

urlpatterns += [
    path('swagger/', schema_view)
]
