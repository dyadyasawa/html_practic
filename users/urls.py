from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.forms import LoginCustomForm
from users.views import RegisterView, RegisterMessageView, UsersListView, email_verification, UserDetailView, \
    UserDeleteView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path('register_message/', RegisterMessageView.as_view(), name='register-message'),
    path('register/email_confirm/<str:token>/', email_verification, name='email-confirm'),

    path('login/', LoginView.as_view(template_name='users_app/login.html', form_class=LoginCustomForm), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('list/', UsersListView.as_view(), name='users-list'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),

    # path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    # path("detail/<int:pk>/", UserDetailApiView.as_view(), name="detail"),
    # path("update/<int:pk>/", UserUpdateApiView.as_view(), name="update"),
    # path("delete/<int:pk>/", UserDeleteApiView.as_view(), name="delete"),
    #
    # path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    # path("list/", UserListApiView.as_view(), name="list"),
]
