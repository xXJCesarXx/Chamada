from django.urls import path
from django.contrib.auth import views as auth_views
from .views import criar_usuario

urlpatterns=[
    path('criar_usuario/', criar_usuario, name='criar_usuario')

]