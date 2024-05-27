from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name = 'index'),
        path('signup', views.signup, name = 'signup'),
        path('login', views.login, name = 'login'),
        path('logout', views.logout, name = 'logout'),
        path('home', views.home, name='home'),
        path('<str:room>/', views.room, name='room'),
        path('checkview', views.checkview, name='checkview'),
        path('send', views.send, name='send'),
        path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]
