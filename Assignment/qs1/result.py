
from django.dispatch import Signal

#  custom signal
my_signal = Signal()

import datetime
from django.shortcuts import HttpResponse
from .signals import my_signal # type: ignore

def my_result(request):
    print(f"Before signal @: {datetime.datetime.now()}")
    my_signal.send(sender=None)
    print(f"After signal @: {datetime.datetime.now()}")
    return HttpResponse("Signal sent")
