#from django.template.loader import get_template
from django.shortcuts import render_to_response #this is a wrapper around get_template
#from django.template import Context
#from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html');
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #t = get_template('hours_ahead.html');
    #html =  t.render(Context({'hour_offset': offset, 'next_time':dt}))
    #return HttpResponse(html)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time':dt})






