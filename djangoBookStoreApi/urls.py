from django.urls import path
from .views import test_view, UserProfileView

# add route paths here
urlpatterns = [
    path('test/', test_view),
    path('user/<int:user_id>/profile', UserProfileView.as_view()),
]
