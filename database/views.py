from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def execute_sql(request):
    if request.method == "POST":
        sql_command = request.POST.get('sql', '')
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
            return JsonResponse({'status': 'success', 'message': 'SQL command executed successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


def list_tables(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

    table_list = []
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns_count = len(cursor.fetchall())
        table_list.append({
            'name': table_name,
            'columns_count': columns_count,
        })

    return JsonResponse(table_list, safe=False)

def home(request):
    return render(request, 'index.html')

def create_table(request):
    if request.method == "POST":
        table_name = request.POST.get('table_name', '')
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT)")
            return JsonResponse({'status': 'success', 'message': f"Таблиця '{table_name}' створена!"})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

def delete_table(request):
    if request.method == "POST":
        table_name = request.POST.get('table_name', '')
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"DROP TABLE {table_name}")
            return JsonResponse({'status': 'success', 'message': f"Таблиця '{table_name}' видалена!"})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})