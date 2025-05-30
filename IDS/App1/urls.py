from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('identities/', views.identity_table_view, name='identity-table'),
]
