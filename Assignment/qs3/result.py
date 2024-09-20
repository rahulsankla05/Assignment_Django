
from django.db import transaction
from django.shortcuts import HttpResponse
from .models import MyModel # type: ignore
from django.db import connection

def my_view(request):
    try:
        with transaction.atomic():
            obj = MyModel.objects.create(name="Test")
            raise Exception("Force rollback")  # Simulate an exception to roll back the transaction
    except Exception as e:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM my_table_log")
            logs = cursor.fetchall()
        return HttpResponse(f"Transaction rolled back but logs: {logs}")
