from django.urls import path

from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('<int:pid>/', views.postDetails, name='postDetails'),
    ]