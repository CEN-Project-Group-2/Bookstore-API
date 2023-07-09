from django.urls import path
from .views.test_views import test_view
from .views.shopping_carts_view import shopping_carts_view
from .views.user_profile_view import UserProfileView
from .views.wish_list_books_view import wish_list_books_view
from .views.books_view import books_view
from .views.book_details_view import book_details_view

# add route paths here
urlpatterns = [
    path('test/', test_view),
    path('user/<int:id>/shopping_carts', shopping_carts_view),
    path('user/<int:user_id>/profile', UserProfileView.as_view(), name='user_profile'),
    path('user/<int:id>/wishlist', wish_list_books_view),
    path('books/', books_view),
    path('books/<int:id>/details', book_details_view),
]
