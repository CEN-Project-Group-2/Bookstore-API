
from django.urls import path
from .views.test_views import test_view
from .views.shopping_carts_view import ShoppingCartsView, GetAllShoppingCartsView
from .views.user_profile_view import UserProfileView
from .views.user_profile_view import CreateUserView
from .views.user_profile_view import UserDetailView
from .views.user_profile_view import CreateCreditCardView
from .views.user_profile_view import UserUpdateView
from .views.wish_list_books_view import wish_list_books_view, add_book_to_wishlist, create_new_wishlist, delete_book_to_cart
from .views.books_view import books_view
from .views.book_details_view import book_details_view, genre_view, best_selling_books, CreateBookDetailsView, get_book_details_by_isbn_view, get_all_book_details_view
from .views.book_comments_view import BookCommentsView
from .views.book_ratings_view import BookRatingsView, discount_books_by_publisher, get_books_by_rating
from .views.author_view import CreateAuthorView, get_book_details_list_given_author_id

urlpatterns = [
    path('test/', test_view),
    path('user/<int:id>/shopping_carts', ShoppingCartsView.as_view()),
    path('user/<int:user_id>/profile', UserProfileView.as_view(), name='user_profile'),
    path('user/create', CreateUserView.as_view(), name='user-create'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:id>/wishlist', wish_list_books_view),
    path('user/wishlist/add_book', add_book_to_wishlist),
    path('user/wishlist/create_wishlist', create_new_wishlist),
    path('user/wishlist/delete_book_to_cart', delete_book_to_cart),
    path('books/', books_view, name='books'),
    path('books/genre/', genre_view, name='genre'),
    path('books/top_sellers/', best_selling_books, name='top_sellers'),
    path('book/ratings/', get_books_by_rating, name='books-by-rating'),
    path('book/discount/', discount_books_by_publisher, name='discount-books'),
    path('books/<int:id>/details', book_details_view),
    path('user/create-credit-card', CreateCreditCardView.as_view(), name='create_credit_card'),
    path('user/<int:user_id>/update', UserUpdateView.as_view(), name='user-update'),
    path('book/<int:id>/comments', BookCommentsView.as_view(), name='book_comments'),
    path('book/<int:id>/ratings', BookRatingsView.as_view()),
    path('books', CreateBookDetailsView.as_view()),
    path('books/details', get_book_details_by_isbn_view),
    path('book/details', get_all_book_details_view),
    path('author/creator', CreateAuthorView.as_view()),
    path('author/<int:author_id>', get_book_details_list_given_author_id),
    path('user/<int:id>/shopping_carts/books', GetAllShoppingCartsView.as_view()),
]
