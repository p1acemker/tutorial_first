
from django.urls import path, include
from . import views

urlpatterns = [
    # url name will realte to the view's function,especially for redirect
    # and for the a href in html
    # eg:
    # <a href="{% url 'add_cart' cart_item.product.id %}"
    path('', views.cart,name='cart'),
    path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),

]

# print(urlpatterns)