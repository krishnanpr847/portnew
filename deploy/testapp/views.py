from django.shortcuts import render
import datetime
# Create your views here.
def home_view(request):
    date=datetime.datetime.now()
    return render(request,'home.html',{'date':date})