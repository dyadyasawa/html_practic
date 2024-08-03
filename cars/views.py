# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# from cars.paginations import CustomPagination
# from cars.serializers import ProductSerializer
# from cars.models import Product


# class StartPageAPIView(APIView):
class StartPage(TemplateView):
    """ Стартовая страница. """
    template_name = "cars_app/start-page.html"


class Catalog(TemplateView):
    """ Каталог. """
    template_name = "cars_app/base.html"


class CarsListView(ListView):
    """ Выводим список машин. """
    pass


class CarDetailView(DetailView):
    """ Выводим выбранную машину. """
    pass


class CarCreateView(CreateView):
    """ Создаем машину. """
    pass


class CarUpdateView(UpdateView):
    """ Редактируем выбранную машину. """
    pass


class CarDeleteView(DeleteView):
    """ Удаляем выбранную машину. """
    pass
