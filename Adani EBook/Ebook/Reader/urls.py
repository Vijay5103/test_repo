from django.urls import path
from django.contrib import admin
from  . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path("", views.simple_upload, name='simple_upload'),
   
    path('', views.home, name='home'),
    path('book', views.book, name='book'),
     path('home', views.home, name='home'),
   
       path('register', views.RegisterView.as_view(), name='register'),
  path("login", views.LoginView.as_view(), name="login"),
  path("AddBook",views.AddBookListview.as_view(),name="AddBook")






]
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)