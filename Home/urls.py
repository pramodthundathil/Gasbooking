from django.urls import path 
from .import views

urlpatterns = [
    path("Index",views.Index,name="Index"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("",views.SignIn,name="SignIn"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("OilcompanyIndex",views.OilcompanyIndex,name="OilcompanyIndex"),
    path("AgencyIndex",views.AgencyIndex,name="AgencyIndex"),
    path("AdminIndex",views.AdminIndex,name="AdminIndex"),
    path("CreateOilCompany",views.CreateOilCompany,name="CreateOilCompany"),
    path("CreateAgency",views.CreateAgency,name="CreateAgency"),
    path("CreateStaff",views.CreateStaff,name="CreateStaff"),
    path("Comapanies",views.Comapanies,name="Comapanies"),
    path("Agency",views.Agency,name="Agency"),
    path("DeleteCompany/<int:pk>",views.DeleteCompany,name="DeleteCompany"),
    path("DeleteAgency/<int:pk>",views.DeleteAgency,name="DeleteAgency"),

    
    
    
]  