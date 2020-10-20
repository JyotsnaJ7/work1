from django.shortcuts import render,redirect
from bdologin.forms import LeadCreateFrm,RegistrationFrm,FollowupFrm
from bdologin.models import Lead,Followup
from django.contrib.auth import  authenticate,login

# Create your views here.

def createLead(request):

    form=LeadCreateFrm()
    context={}
    context['form']=form
    qs = Lead.objects.all()
    context['leads'] = qs

    if request.method=='POST':
        form=LeadCreateFrm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createlead')

    return render(request,'bdologin/leadreg.html',context)

def register(request):
    form=RegistrationFrm()

    context={}
    context['form']=form

    if request.method=='POST':
        form=RegistrationFrm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
        else:
            context['form']=form
            return render(request, 'bdologin/registration.html', context)
    return render(request,'bdologin/registration.html',context)

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        print(username,',',password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('createlead')
        else:
            return redirect('loginpage')

    return render(request,'bdologin/login.html')


def leadDetails(request,pk):
    obj=Lead.objects.get(id=pk)

    context={}
    context['lead']=obj

    return render(request,'bdologin/leaddetails.html',context)

def leadEdit(request,pk):
    form=Lead.objects.get(id=pk)
    form=LeadCreateFrm(instance=form)

    context={'Edit':form}
    if request.method == "POST":
        form=Lead.objects.get(id=pk)
        form=LeadCreateFrm(instance=form,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createlead')
    return render(request,'bdologin/leadedit.html',context)


def createFollowUp(request):

    form=FollowupFrm
    context={}
    context['form']=form
    qs = Followup.objects.all()
    context['followups'] = qs

    if request.method=='POST':
        form=FollowupFrm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createlead')
    return render(request, 'bdologin/followupcreate.html', context)

def followupView(request,pk):
    obj=Followup.objects.get(id=pk)

    context={}
    context['followup']=obj

    return render(request,'bdologin/followupview.html',context)

def followupDelete(request,pk):
    dele=Followup.objects.get(id=pk)
    dele.delete()
    form=FollowupFrm()
    context={'form':form}
    qs=FollowupFrm()
    context['delete']=qs
    return redirect('createfollowup')