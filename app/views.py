from django.shortcuts import render
import datetime
# Create your views here.
def filters(request):
    da=datetime.datetime.now()
    d={'data':'ThIs Is My DaTa','da':da,'c':10}
    return render(request,'filters.html',d)