from django.urls import path
from . import views

urlpatterns = [
    #path('', include('quotes.urls'))
    path('', views.HomeView.as_view(), name = "home")
]
