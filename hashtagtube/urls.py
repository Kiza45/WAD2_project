from django.urls import path
from hashtagtube import views

app_name = 'hashtagtube'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/',views.register, name='register'),
    path('category/<slug:category_name_slug>/',
    	 views.show_category, name='show_category'),
    path('add_category/',views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_video/',
    	  views.add_video, name='add_video'),
    path('restricted/',views.restricted, name='restricted'),
    path('logout/',views.user_logout, name='logout'),
]
