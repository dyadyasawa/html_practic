# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# from cars.paginations import CustomPagination
# from cars.serializers import ProductSerializer
# from cars.models import Product


# class StartPageAPIView(APIView):
class StartPage(TemplateView):
    template_name = "products_app/start-page.html"
