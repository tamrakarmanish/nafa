from django.db import models
from main.models import Membership
# Create your models here.

    
class Order(models.Model):
    product = models.ForeignKey(Membership, max_length=200,on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.product.name
    