from django.shortcuts import render
from django.http import HttpResponse
import redis

from .models import School
# Create your views here.

rds = redis.StrictRedis('redisdb', 6379)


def hello(request):
    rds.incr('count', 1)
    cnt = rds.get('count')
    cnt = b'0' if cnt is None else cnt
    res = School.objects.values_list('school_name', flat=True)
    context = {'cnt': cnt, 'res': res}
    return render(request, 'index.html', context)

