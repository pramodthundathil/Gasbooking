from django.db import models
from django.contrib.auth.models import User


class GasCylinder(models.Model):
    """
    Model for storing gas cylinder information and stock details.
    """

    TYPE_CHOICES = (
        ('LPG', 'Liquefied Petroleum Gas'),
        ('CNG', 'Compressed Natural Gas'),
        ('Industrial', 'Industrial Gas'),
        ('Other', 'Other'),
    )

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='LPG')
    brand = models.CharField(max_length=50)
    weight = models.PositiveIntegerField(help_text="Weight in kilograms")
    stock_level = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return f"{self.type} cylinder - {self.brand} ({self.weight} kg)"
    

class AgencyStock(models.Model):
    Gas = models.ForeignKey(GasCylinder,on_delete = models.CASCADE)
    stock = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    price = models.PositiveIntegerField(null = True)
    appovel = models.BooleanField(default = False)

    def __str__(self):
        return str(self.Gas) + " Price: " + str(self.price)

class BookGas(models.Model):
    Gas = models.ForeignKey(AgencyStock,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    requested_date = models.DateField(auto_now_add = True)
    approval_status = models.BooleanField(default = False)
    status = models.CharField(max_length = 30,default = "Booked Not Approved" )
    deliverydate = models.DateField(auto_now = False, null = True)

    

