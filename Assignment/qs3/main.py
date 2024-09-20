'''Django signals dont run automatically  in the same Fatabase transaction as the caller, 
They are executed independently of the transaction unless explicitly managed within
 a transaction block.
'''
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)