# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# from rest_framework.response import Response
from django.urls import reverse_lazy
from rest_framework.views import APIView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from cars.forms import CarForm
# from cars.paginations import CustomPagination
# from cars.serializers import ProductSerializer
from cars.models import Car, Category


# class StartPageAPIView(APIView):
class StartPage(TemplateView):
    """ Стартовая страница. """
    template_name = "cars_app/start_page.html"


class CarsListView(ListView):
    """ Выводим список машин. """

    model = Car
    template_name = "cars_app/cars_list.html"


class CarsCategoriesListView(ListView):
    """ Выводим список машин определенной категории. """

    model = Category
    template_name = "cars_app/cars_list_categories.html"

    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        id_category = self.kwargs.get("pk")  # Получаем id категории из-под которой заходим

        queryset = queryset.get(pk=id_category)  # Получаем единственную категорию по id

        queryset = queryset.car_set.all()  # Формируем queryset из элементов модели Car с заданной категорией (по id)

        return queryset


class CarDetailView(DetailView):
    """ Выводим выбранную машину. """

    model = Car
    template_name = "cars_app/car_detail.html"


class CarCreateView(CreateView):
    """ Создаем машину. """

    model = Car
    template_name = 'cars_app/car_form.html'
    form_class = CarForm
    success_url = reverse_lazy('cars:list')


class CarUpdateView(UpdateView):
    """ Редактируем выбранную машину. """
    pass


class CarDeleteView(DeleteView):
    """ Удаляем выбранную машину. """
    pass


class CategoryList(ListView):
    """ Выводим список категорий. """

    model = Category
    template_name = "cars_app/category_list.html"
