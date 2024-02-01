from django.conf.urls import url 
from django.urls import path
from testapp import views

urlpatterns = [
    path('first/', views.display1),
    path('second/', views.display2),
    path('third/', views.display3),
    path('fourth/', views.display4),
    path('fiveth/', views.display5),
    path('mywish/', views.wish)
]