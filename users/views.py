
import random

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DetailView, DeleteView

# from rest_framework.generics import (
#     CreateAPIView,
#     DestroyAPIView,
#     ListAPIView,
#     RetrieveAPIView,
#     UpdateAPIView,
# )
# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

from config import settings
from config.settings import EMAIL_HOST_USER
from users.forms import RegisterForm, UserForm, MessageForm
from users.models import User, Message


# from users.paginations import CustomPagination
# from users.serializers import UserSerializer


class RegisterView(CreateView):
    """ Регистрируем пользователя. """

    model = User
    template_name = 'users_app/user_form.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:register-message')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        token = "".join([str(random.randint(0, 9)) for i in range(10)])
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/register/email_confirm/{token}/'
        send_mail(
            'Подтверждение почты',
            f'Перейдите по ссылке для подтверждения почты {url}',
            EMAIL_HOST_USER,
            [user.email],
        )
        return super().form_valid(form)


class RegisterMessageView(TemplateView):

    template_name = 'users_app/register_message.html'


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    # return redirect(reverse('users:login'))
    return HttpResponseRedirect('/users/login/')


class UsersListView(UserPassesTestMixin, ListView):

    model = User
    template_name = 'users_app/users_list.html'

    def test_func(self):
        user =self.request.user
        return user.is_superuser


class UserDetailView(DetailView):

    model = User
    template_name = 'users_app/user_detail.html'


class UserUpdateView(UserPassesTestMixin, UpdateView):

    model = User
    template_name = 'users_app/user_form.html'
    form_class = UserForm
    success_url = reverse_lazy('users:users-list')

    def test_func(self):
        user =self.request.user
        return user.is_superuser


class UserDeleteView(UserPassesTestMixin, DeleteView):

    model = User
    template_name = 'users_app/user_confirm_delete.html'
    success_url = reverse_lazy('users:users-list')

    def test_func(self):
        user =self.request.user
        return user.is_superuser


class MessageForUserView(UpdateView):
    model = User
    form_class = MessageForm
    template_name = 'users_app/send_message_form.html'
    success_url = reverse_lazy('users:users-list')
    
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

    # def form_valid(self, form):
    #     message = form.save()
    #     email_for_send = message.addressee.email
    #     text = message.message
    #     message.save()
    #
    #     send_mail(
    #         'Сообщение от Admin',
    #         f'{text}',
    #         EMAIL_HOST_USER,
    #         [email_for_send],
    #     )
    #     print(email_for_send)
    #     return super().form_valid(form)
