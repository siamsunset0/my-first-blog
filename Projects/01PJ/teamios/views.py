from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import SimpleInfo
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def si_list(request):
    simpleinfos = SimpleInfo.objects.order_by('id')
    rtStrValue = simpleinfos[0].siLabel
    return HttpResponse(rtStrValue)
