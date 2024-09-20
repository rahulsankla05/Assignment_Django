from django.dispatch import Signal

# Define a custom signal
my_signal = Signal()

# views.py
import datetime
from django.shortcuts import HttpResponse
from .signals import my_signal # type: ignore

def my_view(request):
    print(f"Before signal at: {datetime.datetime.now()}")
    my_signal.send(sender=None)
    print(f"After signal at: {datetime.datetime.now()}")
    return HttpResponse("Signal sent")


