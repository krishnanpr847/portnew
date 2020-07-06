from django.shortcuts import render
from testapp.models import port_model
from testapp.forms import signup_form
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
#@login_required
def home_view(request):
    return render(request,'home.html')
@login_required
def feedback_view(request):
    if request.method=='POST':
        
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        feedback=request.POST['feedback']
        print(name,email,phone,feedback)
        ins=port_model(name=name,email=email,phone=phone,feedback=feedback)
        ins.save()
        print("SUCCESSFULLY THE FEEDBACK HAS BEEN SENT....")   
        return home_view(request)
        
    return render(request,'feedback.html')

def signup_view(request):
    form=signup_form()
    if request.method=='POST':
        form=signup_form(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()

        return HttpResponseRedirect('/accounts/login')
    
    return render(request,'signup.html',{'form':form})
        
