from django.urls import path
from . import views


urlpatterns = [
    path('', views.funko_pop_list, name='funko_pop_list'),
]