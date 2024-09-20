# receivers.py
from django.db import models
from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel # type: ignore

@receiver(post_save, sender=MyModel)
def my_model_signal_handler(sender, instance, **kwargs):
    with connection.cursor() as cursor:
        # Directly insert into the database to simulate a change inside the signal
        cursor.execute("INSERT INTO my_table_log (action) VALUES ('Signal executed')")
