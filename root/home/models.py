from django.db import models

# Create your models here.

class Brands(models.Model):
    manufacturer = models.CharField(max_length=40)
    catagory = models.CharField(max_length=40)
    items_list = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.manufacturer} {self.catagory} {self.items_list}"
class ProductDetails(models.Model):
    storage = models.IntegerField(max_length=3)
    camera = models.IntegerField(max_length=3)
    ram = models.IntegerField(max_length=3)
    def __str__(self):
        return f"Rom {self.storage} GB"
    def __str__(self):
        return f"RAM {self.ram} GB"
    def __str__(self):
        return f"Camera {self.camera} MP"
class Products(models.Model):
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=40)
#    Product_Catagory = models.ForeignKey(Brands, on_delete=models.CASCADE)
    Capacity = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.id} {self.brand_name} {self.model_name} {self.Capacity}"
