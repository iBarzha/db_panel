from django.urls import path
from .views import execute_sql, list_tables, home, create_table, delete_table

urlpatterns = [
    path('tables/', list_tables, name='list_tables'),
    path('execute_sql/', execute_sql, name='execute_sql'),
    path('', home, name='home'),
    path('create_table/', create_table, name='create_table'),
    path('delete_table/', delete_table, name='delete_table'),
]