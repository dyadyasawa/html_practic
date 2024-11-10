
from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User, Message


class StyleMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name != "is_superuser" and field_name != "is_staff" and field_name != "is_active":
                field.widget.attrs["class"] = "form-control"


class RegisterForm(StyleMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class LoginCustomForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

# class UserRegisterForm(StyleMixin, UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = ('email', 'password1', 'password2',)
#
#
# class PasswordRecoveryForm(StyleMixin, forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = ('email',)


class UserForm(StyleMixin):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ("email", "city", "phone", "avatar", "is_superuser", "is_staff", "is_active")


class MessageForm(StyleMixin):
    class Meta:
        model = Message
        fields = ("message",)
