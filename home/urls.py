from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('games/', views.all_games,name='games'),
    path('games_post/<int:id>',views.games_post,name='games_post'),
    path('login/', views.handle_login,name='login'),
    path('signup/', views.handle_signup,name='signup'),
    path('logout/', views.handle_logout,name='logout'),
    path('comments/', views.handle_comments,name='comment'),
    path('replies/', views.handle_replies,name='reply'),

]
