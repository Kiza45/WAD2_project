from django.urls import path
from hashtagtube import views

app_name = 'hashtagtube'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/',views.register, name='register'),
]
