from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListCreate.as_view(), name='book-list-create'),
    path('<int:pk>/', views.BookRetrieveUpdateDelete.as_view(), name='book-detail'),
]
