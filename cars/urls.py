
from django.urls import path
# from rest_framework.permissions import AllowAny

from cars.apps import CarsConfig
from cars.views import StartPage, Catalog, CarsListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

app_name = CarsConfig.name

urlpatterns = [
    path("", StartPage.as_view(), name="start-page"),
    path("catalog/", Catalog.as_view(), name="catalog"),


    # path("list/", CarsListView.as_view(), name="cars-list"),
    # path("detail/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    # path("create/", CarCreateView.as_view(), name="car-create"),
    # path("update/<int:pk>/", CarUpdateView.as_view(), name="car-update"),
    # path("delete/<int:pk>/", CarDeleteView.as_view(), name="car-delete"),
]
