from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [

    path('', views.BooksView.as_view(), name='main'),
    path('detail/<int:pk>', views.BooksDetailView.as_view(), name = 'books_detail'),
    path('detail/<int:id>/read', views.read, name='read'),
    path('add',  views.add_view, name='add'),
    path('detail/<int:pk>/delete', views.BookDelete.as_view(), name= 'delete'),
    path('detail/<int:pk>/update', views.BooksUpdate.as_view(), name = 'update')
]