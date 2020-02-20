from django.urls import path
from . import views

urlpatterns = [
    # When only domain name is provided, check home view in views.py to carryout the action
    path('', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
]
