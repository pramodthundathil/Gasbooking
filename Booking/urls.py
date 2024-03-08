from django.urls import path  
from .import views  

urlpatterns = [
    
    path("OilCompanyStock",views.OilCompanyStock,name="OilCompanyStock"),
    path("update_stock/<int:pk>",views.update_stock,name="update_stock"),
    path("AgencyStocks",views.AgencyStocks,name="AgencyStocks"),
    path("RefillRequest",views.RefillRequest,name="RefillRequest"),
    path("ApproveRefillRequest/<int:pk>",views.ApproveRefillRequest,name="ApproveRefillRequest"),
    path("CustomerBooking",views.CustomerBooking,name="CustomerBooking"),
    path("CustomerBookingAgencyView",views.CustomerBookingAgencyView,name="CustomerBookingAgencyView"),
    path("ApproveBooking/<int:pk>",views.ApproveBooking,name="ApproveBooking"),
    path("UpdateStatus/<int:pk>",views.UpdateStatus,name="UpdateStatus"),

    
]