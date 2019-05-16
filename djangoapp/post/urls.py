from django.urls import path

from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('rest/', views.postRestData, name='postRestData'),
    path('<int:pid>/', views.postDetails, name='postDetails'),
    ]