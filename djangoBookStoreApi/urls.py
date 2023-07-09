from django.urls import path
from .views.test_views import test_view
from .views.shopping_carts_view import shopping_carts_view
from .views.user_profile_view import UserProfileView
from .views.wish_list_books_view import wish_list_books_view
from .views.books_view import books_view, genre_view, best_selling_books

# add route paths here
urlpatterns = [
    path('test/', test_view),
    path('user/<int:id>/shopping_carts', shopping_carts_view),
    path('user/<int:user_id>/profile', UserProfileView.as_view(), name='user_profile'),
    path('user/<int:id>/wishlist', wish_list_books_view),
    path('books/', books_view, name='books'),
    path('books/genre/', genre_view, name='genre'),
    path('books/top_sellers/', best_selling_books, name='top_sellers')
]
