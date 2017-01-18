from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import SimpleInfo

# Create your views here.
def si_list(request):
    simpleinfos = SimpleInfo.objects.order_by('id')
    rtStrValue = simpleinfos[0].siLabel
    return HttpResponse(rtStrValue)
