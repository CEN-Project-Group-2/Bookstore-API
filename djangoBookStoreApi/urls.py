from django.urls import path
from .views.test_views import test_view
from .views.shopping_carts_view import shopping_carts_view

# add route paths here
urlpatterns = [
    path('test/', test_view),
    path('user/<int:id>/shopping_carts', shopping_carts_view),
]
