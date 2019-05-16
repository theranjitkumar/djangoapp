from django.urls import path

from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    # path('<id>/', views.postById, name='post'),
    ]