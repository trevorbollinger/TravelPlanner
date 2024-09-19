from django.urls import path
from . import views

urlpatterns = [
    # at localhost/ hello_view from views.py is called
    path('', views.hello_view, name='hello'),

    # at localhost/api-demo/, api_demo_view is called from views.py is called
    path('api-demo/', views.api_demo_view, name='api_demo')
]
