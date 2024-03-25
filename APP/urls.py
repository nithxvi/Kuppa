from django.urls import path
from . import views

urlpatterns =[
    
    path('', views.Landing, name='Home'),
    path('Register', views.Register, name='Register'),
    path('Login', views.Login, name='Login'),
    path('Prompt', views.prompt_page, name='Deploy')
]