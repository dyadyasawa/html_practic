# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# from rest_framework.response import Response
from django.urls import reverse_lazy
from rest_framework.views import APIView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from cars.forms import CarForm, CategoryForm
# from cars.paginations import CustomPagination
# from cars.serializers import ProductSerializer
from cars.models import Car, Category

# Стартовая страница сайта


class StartPage(TemplateView):
    """ Стартовая страница. """
    template_name = "cars_app/start_page.html"

# CRUD для модели Car


class CarsListView(ListView):
    """ Выводим список машин. """

    model = Car
    template_name = "cars_app/cars_list.html"


class CarDetailView(DetailView):
    """ Выводим выбранную машину. """

    model = Car
    template_name = "cars_app/car_detail.html"


class CarCreateView(CreateView):
    """ Создаем машину. """

    model = Car
    template_name = 'cars_app/car_form.html'
    form_class = CarForm
    success_url = reverse_lazy('cars:cars-list')

    def form_valid(self, form):

        car = form.save()
        car.owner = self.request.user
        car.save()

        # context_data = self.get_context_data()
        # formset = context_data['formset']
        #
        # if formset.is_valid():
        #     formset.instance = car
        #     formset.save()
        return super().form_valid(form)


class CarUpdateView(UpdateView):
    """ Редактируем выбранную машину. """

    model = Car
    template_name = 'cars_app/car_form.html'
    form_class = CarForm
    success_url = reverse_lazy('cars:cars-list')


class CarDeleteView(DeleteView):
    """ Удаляем выбранную машину. """

    model = Car
    template_name = 'cars_app/car_confirm_delete.html'
    success_url = reverse_lazy('cars:cars-list')

# CRUD для модели Category


class CategoryList(ListView):
    """ Выводим список категорий. """

    model = Category
    template_name = "cars_app/category_list.html"


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


class CategoryCreateView(CreateView):
    """ Создаем категорию. """

    model = Category
    template_name = 'cars_app/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('cars:category-list')


class CategoryUpdateView(UpdateView):
    """ Редактируем выбранную категорию. """

    model = Category
    template_name = 'cars_app/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('cars:category-list')


class CategoryDeleteView(DeleteView):
    """ Удаляем выбранную категорию. """

    model = Category
    template_name = 'cars_app/category_confirm_delete.html'
    success_url = reverse_lazy('cars:category-list')
