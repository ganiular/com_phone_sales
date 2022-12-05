from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    old_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img/product/")

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.phone.name + ' (' + str(self.quantity) + ')'  
