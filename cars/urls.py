
from django.urls import path
# from rest_framework.permissions import AllowAny

from cars.apps import ProductsConfig
from cars.views import StartPage

app_name = ProductsConfig.name

urlpatterns = [
    path("", StartPage.as_view(), name="start-page"),
]
