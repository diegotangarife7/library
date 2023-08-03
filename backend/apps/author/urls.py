from django.urls import path

from . import views




urlpatterns = [
    #author/
    path('create/', views.CreateAuthorAPIView.as_view(), name='create_author'),
    path('list/', views.ListAllAuthorAPIView.as_view(), name='list_authors'),
    path('update/<int:pk>/', views.UpdateAuthorAPIView.as_view(), name='update_author'),
]
