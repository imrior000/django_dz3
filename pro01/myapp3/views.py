import datetime
from django.shortcuts import render
from django.http import HttpResponse
from myapp3.models import Order

date_t = str(datetime.datetime.today()).split()[0]
yy, mm, dd = date_t.split('-')
yy = int(yy)
mm = int(mm)
dd = int(dd)

def index(request):
    res =  Order.objects.all()
    http={'qwerty': res}
    return render(request, 'myapp3/my_template.html', http)

def day(request):
    res =  Order.objects.filter(date_ordered__range=(datetime.date(yy, mm, dd) - datetime.timedelta(days=7), datetime.date(yy, mm, dd)))
    http={'qwerty': res}
    return render(request, 'myapp3/my_template.html', http)

def month(request):
    res =  Order.objects.filter(date_ordered__range=(datetime.date(yy, mm, dd) - datetime.timedelta(days=30), datetime.date(yy, mm, dd)))
    http={'qwerty': res}
    return render(request, 'myapp3/my_template.html', http)

def year(request):
    res =  Order.objects.filter(date_ordered__range=(datetime.date(yy, mm, dd) - datetime.timedelta(days=365), datetime.date(yy, mm, dd)))
    http={'qwerty': res}
    return render(request, 'myapp3/my_template.html', http)