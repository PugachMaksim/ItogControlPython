from django.urls import path
from .views import about, home, add_recept, edit_recept, recept
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('addrecept.html/', add_recept, name='add_recept'),
    path('edit_recept/<int:recept_id>', edit_recept, name='edit_recept'),
    path('recept/<int:recept_id>', recept, name='recept')
]
