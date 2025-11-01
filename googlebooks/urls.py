from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.import_books_view, name='import_books'),
    path('api/books/', views.books_json, name='books_json'),
]
