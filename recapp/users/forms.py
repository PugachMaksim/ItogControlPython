from django import forms
from .models import Recept, CategoryRecept


class AddRecept(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=CategoryRecept.objects.all(), label='Категория',
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'form-control', 'placeholder': 'Блюдо'}))
    recept_name = forms.CharField(label='Название рецепта',
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Блюдо'}))
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control', 'placeholder': 'Описание рецепта'}))
    image = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={'class': 'form-control'}))
    ingredients = forms.CharField(label='Ингредиенты',
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ингредиенты'}))
    cooking_steps = forms.CharField(label='Приготовление',
                                    widget=forms.Textarea(
                                        attrs={'class': 'form-control', 'placeholder': 'Приготовление'}))
    cooking_time = forms.CharField(label='Время приготовления', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Время приготовления'}))

    class Meta:
        model = Recept
        # fields = ['recept_name', 'category', 'description', 'image', 'ingredients', 'cooking_steps', 'cooking_time']
        exclude = ["author"]
