from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .models import DatabaseTable

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
    tables = DatabaseTable.objects.all().values("name", "columns_count", "created_at")
    return JsonResponse(list(tables), safe=False)

def home(request):
    return render(request, 'index.html')
