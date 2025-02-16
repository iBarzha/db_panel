from django.urls import path
from .views import execute_sql, list_tables, home

urlpatterns = [
    path('tables/', list_tables, name='list_tables'),
    path('execute_sql/', execute_sql, name='execute_sql'),
    path('', home, name='home'),
]