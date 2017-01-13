from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import SimpleInfo

# Create your views here.
def si_list(request):
    simpleinfos = SimpleInfo.objects
    return render(response, simpleinfos)
