
from django.urls import path
from . import views


urlpatterns = [
    
    #path('',include('main_app.urls'))
    #path('', views.homeView, name='Home'),
    #path('home/', views.homeView, name='Home'),
    #path('', views.HomeView.as_view()),
    path('', views.HomeView.as_view(), name="home"),
    path('about/', views.AboutMe.as_view(), name="about"),
]
