from django.urls import path
from hashtagtube import views

app_name = 'hashtagtube'

urlpatterns = [
    path('', views.index, name='index'),
   #path('login/', views.user_login, name='login'),
   #path('register/',views.register, name='register'),
    path('category/<slug:category_name_slug>/',
    	 views.show_category, name='show_category'),
    path('add_category/',views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_video/',
    	  views.add_video, name='add_video'),
    path('restricted/',views.restricted, name='restricted'),
   #path('logout/',views.user_logout, name='logout'),
    path('like_video/', views.like, name='like_video'),
    path('dislike_video/', views.dislike, name='dislike_video'),
    path('love_video/', views.love, name='love_video'),
    path('haha_video/', views.haha, name='haha_video'),
    path('follow_unfollow/', views.follow_unfollow, name='follow_unfollow'),
    path('submit_comment/', views.submit_comment, name='submit_comment'),
    path('profile/', views.profile, name='profile'),
    path('video/<int:video_id>/', views.video, name='video'),    
]
