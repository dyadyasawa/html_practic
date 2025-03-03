# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
           # !!!!! from rest_framework.views import APIView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from cars.forms import CarForm, CategoryForm, MessageForm
# from cars.paginations import CustomPagination
# from cars.serializers import ProductSerializer
from cars.models import Car, Category
from config.settings import EMAIL_HOST_USER


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


class CarCreateView(LoginRequiredMixin, CreateView):
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


class CarUpdateView(LoginRequiredMixin, UpdateView):
    """ Редактируем выбранную машину. """

    model = Car
    template_name = 'cars_app/car_form.html'
    form_class = CarForm
    success_url = reverse_lazy('cars:cars-list')


class CarDeleteView(LoginRequiredMixin, DeleteView):
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


class MessageForUserView(UpdateView):
    """ Отправляем сообщение пользователю. """

    model = Car
    form_class = MessageForm
    template_name = 'cars_app/send_message_form.html'
    success_url = reverse_lazy('cars:cars-list')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['email_for_send'] = self.request.user.email
    #     return context

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #
    #     id_addressee = self.kwargs.get("pk")
    #
    #     return queryset

    def form_valid(self, form):
        car = form.save()
        message = car.message_for_owner
        email = car.owner.email
        car.save()
        # print(f'Будет отправлено сообщение: "{message}", по адресу: "{email} "')
        send_mail(
            'Сообщение от админа',
            f'Админ говорит: {message}',
            EMAIL_HOST_USER,
            [email],
        )
        car.message_for_owner = None
        car.save()
        return super().form_valid(form)

    # def messages_delete(request):
    #     """ Удаляем все сообщения для владельцев. """
    #
    #     for object in Car.objects.all():
    #         object.message_for_owner = None
    #         object.save()
