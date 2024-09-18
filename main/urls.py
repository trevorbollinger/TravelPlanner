from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_view, name='hello'),
    path('api-demo/', views.api_demo, name='api_demo'),
]
