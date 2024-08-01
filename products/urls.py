
from django.urls import path
# from rest_framework.permissions import AllowAny

from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path("", StartPageAPIView.as_view(), name="start-page"),
]
