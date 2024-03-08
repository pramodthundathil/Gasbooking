from django.shortcuts import render, redirect
from .models import GasCylinder, AgencyStock, BookGas
from .forms import GasCylinderForm, AgencyStockRequestForm, GasBookForm
from django.contrib import messages
from datetime import datetime


# Create your views here.

# oil company Workings

def OilCompanyStock(request):
    form = GasCylinderForm()

    gas = GasCylinder.objects.filter(user = request.user)

    if request.method == "POST":
        form = GasCylinderForm(request.POST)
        if form.is_valid():
            gas = form.save()
            gas.user = request.user
            gas.save()
            messages.info(request,'Gas Cylinder Added.....')
            return redirect('OilCompanyStock')


    context = {
        "form":form,
        "gas":gas
    }
    return render(request,"oilcompanystock.html",context)

from django.shortcuts import render, redirect

def update_stock(request, pk):
    if request.method == 'POST':
        delta = request.POST['stock']
        try:
            cylinder = GasCylinder.objects.get(pk=pk)
            cylinder.stock_level += int(delta)
            cylinder.save()
            messages.info(request,"Stock Updated......")
            return redirect('OilCompanyStock')  # Redirect to success page
        except:
            # Handle the case where the cylinder is not found
            messages.info(request,"not Updated......")
            
    return redirect("OilCompanyStock") # Render update form (if applicable)


def RefillRequest(request):
    gas = AgencyStock.objects.filter(Gas__user = request.user)
    context = {
            
            "gas":gas
    }
    return render(request,"refillrequest.html",context)


def ApproveRefillRequest(request,pk):
    if request.method == "POST":
        price = request.POST["price"]
        req = AgencyStock.objects.get(id = pk)
        req.price = price 
        req.appovel = True
        req.save()
        gas = req.Gas
        gas.stock_level = gas.stock_level - req.stock
        gas.save()
        messages.info(request,'Gas Cylinder Stock Request Approved.....')
        return redirect("RefillRequest")
    return redirect("RefillRequest")



# Agency stock filling and working 


def AgencyStocks(request):
    form = AgencyStockRequestForm()

    gas = AgencyStock.objects.filter(user = request.user)

    if request.method == "POST":
        form = AgencyStockRequestForm(request.POST)
        if form.is_valid():
            gas = form.save()
            gas.user = request.user
            gas.save()
            messages.info(request,'Gas Cylinder Stock Requested.....')
            return redirect('AgencyStocks')
        
    context = {
            "form":form,
            "gas":gas
    }
    return render(request,"agencystock.html",context)




def StockUpdateRequest(request,pk):
    
    if request.method == "POST":
        stock = request.POST['stock']



def CustomerBookingAgencyView(request):
    gas = BookGas.objects.filter(Gas__user = request.user)

    context = {
        "gas":gas
    }
    return render(request,"customerbookings.html",context)

def ApproveBooking(request,pk):
    gas = BookGas.objects.get(id = pk)
    if gas.Gas.stock < 1:
        messages.info(request,'No Stock Please Update Stock')
        return redirect("CustomerBookingAgencyView")
    else:
        gas.approval_status =True
        gas.save()
        st = gas.Gas
        st.stock -= 1
        st.save()
        messages.info(request,'Approved........')
        return redirect("CustomerBookingAgencyView")
    return redirect("CustomerBookingAgencyView")


def UpdateStatus(request, pk):
    gas = BookGas.objects.get(id = pk)
    if request.method == "POST":
        status = request.POST["status"]
        gas.status = status
        gas.save()
        if status == "Delivered":
            gas.deliverydate = datetime.now()
            gas.save()
        messages.info(request,'Status Updated........')
        
        return redirect("CustomerBookingAgencyView")
    
    return redirect("CustomerBookingAgencyView")



# Customer Gas Booking.....


def CustomerBooking(request):
    form = GasBookForm()

    gas = BookGas.objects.filter(user = request.user)

    if request.method == "POST":
        form = GasBookForm(request.POST)
        if form.is_valid():
            if BookGas.objects.filter(user = request.user, deliverydate = None ).exists():
                messages.info(request,'You Already Have Undelivered Booking On this Cylinder  .....')
                return redirect('CustomerBooking')
            else:
                gas = form.save()
                gas.user = request.user
                gas.save()
                messages.info(request,'Gas Booked Wait For Confirmation.....')
                return redirect('CustomerBooking')
        
    context = {
        "form":form,
        "gas":gas
    }
    return render(request,'mybookings.html',context)

