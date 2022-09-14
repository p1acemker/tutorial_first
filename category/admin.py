from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','slug')
    prepopulated_fields = {'slug':('category_name',)}
# # 注册的时候，将原模型和ModelAdmin耦合起来
admin.site.register(Category,CategoryAdmin)