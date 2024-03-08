from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import UserAddForm
from django.contrib.auth.models import User,Group
from .decorators import admin_only,NullGroup,unautenticated_user
from django.http import HttpResponse
from Booking.forms import GasBookForm



@admin_only
def Index(request):
    form = GasBookForm()

    context = {
        "form":form
    }
    return render(request,"index.html",context)



def AgencyIndex(request):
    form = UserAddForm()
    context = {
        "form":form
    }
    return render(request,"agencyindex.html",context)



def OilcompanyIndex(request):
    context = {
        
    }
    return render(request,"oilcompanyindex.html",context)


def AdminIndex(request):
    form = UserAddForm()
    context = {
        "form":form
    }
    return render(request,"adminindex.html",context)


def CreateAgency(request):
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            group = Group.objects.get(name='agency')
            new_user.groups.add(group) 
            messages.info(request,'Agency Created.....')
            return redirect('Index')
        
    return redirect('Index') 

def CreateStaff(request):
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            group = Group.objects.get(name='staff')
            new_user.groups.add(group) 
            messages.info(request,'staff Created.....')
            return redirect('Index')
        
    return redirect('Index') 
    
            

def CreateOilCompany(request):
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            group = Group.objects.get(name='oilcompany')
            new_user.groups.add(group)
            messages.info(request,'Oilcompany Created')
            return redirect('Index') 
        else:
            messages.info(request,'Something Worng.. <br> Check password Minimum 8 chacactors and alphanumeric charectors <br> Also Check Email')
            return redirect('Index')   
        
    return redirect('Index') 



@unautenticated_user
def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
    return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('SignUp')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('SignUp')
            else:
                new_user = form.save()
                new_user.save()
                
                # group = Group.objects.get(name='user')
                # new_user.groups.add(group) 
                
                messages.success(request,"User Created")
                return redirect('SignIn')
            
    return render(request,"register.html",{"form":form})



def SignOut(request):
    logout(request)
    return redirect('SignIn')


# admin views items  


def Comapanies(request):
    companies = User.objects.filter(groups__name = "oilcompany")
    context = {
        "companies":companies
    }
    return render(request,"companies.html", context)

def DeleteCompany(request,pk):
    User.objects.get(id = pk).delete()
    messages.success(request,"User deleted")
    return redirect('Comapanies')

def Agency(request):
    agency = User.objects.filter(groups__name = "agency")
    context = {
        "agency":agency
    }
    return render(request,"agency.html", context)

def DeleteAgency(request,pk):
    User.objects.get(id = pk).delete()
    messages.success(request,"User deleted")
    return redirect('Comapanies')
