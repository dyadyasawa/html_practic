
from django import forms

from cars.models import Car, Category


class StyleMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name != 'current_version_indicator' and field_name != 'publication_sign' and field_name != 'is_published':

                field.widget.attrs["class"] = "form-control"  # Применяем ко всем полям, которые не в if


class CarForm(StyleMixin):

    # Список запрещенных слов
    # forbidden_words_list = [
    #     'казино',
    #     'криптовалюта',
    #     'крипта',
    #     'биржа',
    #     'дешево',
    #     'бесплатно',
    #     'обман',
    #     'полиция',
    #     'радар'
    # ]

    class Meta:
        model = Car
        # fields = '__all__'
        fields = ('name', 'description', 'category', 'price',)

    # def clean_name(self):
    #     cleaned_data = self.cleaned_data['name']
    #
    #     for word in ProductForm.forbidden_words_list:
    #         if word in cleaned_data.lower():
    #             raise forms.ValidationError('В названии присутствуют недопустимые слова.')
    #     return cleaned_data
    #
    # def clean_description(self):
    #     cleaned_data = self.cleaned_data['description']
    #
    #
    #     for word in ProductForm.forbidden_words_list:
    #         if word in cleaned_data.lower():
    #             raise forms.ValidationError('В описании присутствуют недопустимые слова.')
    #     return cleaned_data


class CategoryForm(StyleMixin):

    class Meta:
        model = Category
        fields = '__all__'
        # fields = ('is_published',)


# class ProductDescriptionForm(StyleMixin):
#
#     class Meta:
#         model = Product
#         # fields = '__all__'
#         fields = ('description',)
#
#
# class ProductCategoryForm(StyleMixin):
#
#     class Meta:
#         model = Product
#         # fields = '__all__'
#         fields = ('category',)
#
#
# class BlogForm(StyleMixin):
#
#     class Meta:
#         model = Blog
#         fields = ('title', 'body', 'preview', 'publication_sign', 'view_count',)
#
#
# class VersionForm(StyleMixin):
#
#     class Meta:
#         model = Version
#         fields = '__all__'
