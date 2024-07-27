from django.contrib import admin
from django.urls import path
# from book_api.views import book_list, book_create, book
from book_api.views import BookList, Bookcreate, BookModify

urlpatterns = [
    # path("", book_create),
    # path("list/", book_list),
    # path('<int:pk>/', book),
    
    path("list/", BookList.as_view()),
    path("", Bookcreate.as_view()),
    path("<int:pk>/", BookModify.as_view()),
] 
    