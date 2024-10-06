# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


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
        id_category = self.kwargs.get("pk")
        print(id_category)

        queryset = queryset.get(pk=id_category)
        print(queryset)

        queryset = queryset.car_set.all()
        print(queryset)

        return queryset


class CarDetailView(DetailView):
    """ Выводим выбранную машину. """

    model = Car
    template_name = "cars_app/car_detail.html"


class CarCreateView(CreateView):
    """ Создаем машину. """
    pass


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
