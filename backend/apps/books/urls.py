from django.urls import path

from . import views


urlpatterns = [
    # books/
    path('create/list/', views.BookCreateAPIView.as_view(), name='book_create'),
    path('update/<int:pk>/', views.BookUpdateAPIView.as_view(), name='book_update'),
]
