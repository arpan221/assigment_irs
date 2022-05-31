from django.urls import path
from apiapp import views

urlpatterns = [
    path('data/', views.values,name='values')
]
