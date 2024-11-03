
import random

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

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
from users.forms import RegisterForm
from users.models import User
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
