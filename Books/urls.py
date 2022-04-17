
from django.contrib import admin
from django.urls import path,include
from booksApp.api.views import BooksUpdateAPIView,BooksGetPostAPIView,BooksDeleteAPIView,BooksGetByStatusAPIView
from booksApp.views import login_view, register_view,home_view
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Books API')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('api/', include('accounts.api.urls')),
    path('books/',BooksGetPostAPIView.as_view()),
    path('books/<int:pk>',BooksGetByStatusAPIView.as_view()),
    path('booksDelete/<int:pk>',BooksDeleteAPIView.as_view()),
    path('booksUpdate/<int:pk>',BooksUpdateAPIView.as_view()),
    path('users/',register_view),
    path('login/',login_view),
    path('home/',home_view),
    
    
]

