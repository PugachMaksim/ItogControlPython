from django.contrib import admin
from .models import Recept, CategoryRecept

admin.site.register(Recept)
admin.site.register(CategoryRecept)

# @admin.register(Recept)
# class NewsReceptAdmin(admin.ModelAdmin):
#     exclude = ('author',) # скрыть author поле, чтобы оно не отображалось в форме изменений
#
#     def save_model(self, request, obj, form, change):
#         if not obj.pk:
#             obj.author = request.user
#         super().save_model(request, obj, form, change)