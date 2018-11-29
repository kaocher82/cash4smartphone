from django.db import models

# Create your models here.
'''
class Catagory(models.Model)
    catagory = (
        ( 'Mobile', 'Phone'),
        ( 'Laptop', 'Computer'),
        ( 'Camera', 'DSLR'),
        ( 'Pad', 'Tablet'),
        ('Smart Watch', 'Watch'),
        ('Electronis', 'Home Appliance'),
        )
        catagory = models.CharField(max_length=20, choices=Catagory)
        def __str__(self):
            return f"{self.catagory}"
    '''
class Brands(models.Model):
    manufacturer = models.CharField(max_length=40)


    def __str__(self):
        return f"{self.manufacturer}"
'''
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
'''


class Phones(models.Model):
    Catagory = (
        ( 'Mobile', 'Phone'),
        ( 'Laptop', 'Computer'),
        ( 'Camera', 'DSLR'),
        ( 'Pad', 'Tablet'),
        ('Smart Watch', 'Watch'),
        ('Electronis', 'Home Appliance'),
    )
    catagory = models.CharField(max_length=20, choices=Catagory)
    Brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    PhoneModel = models.CharField(max_length=40)
    OS = (
        ('A', 'Android'),
        ('I', 'IOS'),
        ('M', 'Microsoft'),
    )
    memory = (
        ('1', '1 GB'),
        ('2', '2 GB'),
        ('3', '3 GB'),
        ('4', '4 GB'),
        ('8', '8 GB'),
        ('16', '16 GB'),
        ('32', '32 GB'),
        ('64', '64 GB'),
        ('128', '128 GB'),
        ('256', '256 GB'),
    )
    COLORS = (
        ('Gold', (
            ('Rose', 'Rose Gold'),
        )
         ),
        ('Silver', (
            ('Gold', 'Silver Gold'),
        )
         ),
        ('White', (
            ('Gold', 'White Gold'),
        )
         ),
        ('Blue', (
            ('Royal', 'Royal Blue'),
        )
         ),

        ('Black', (
            ('Gray', 'Gray'),
            ('Midnight', 'Midnight Bkack'),
        )
         ),
        ('Roral', (
            ('Lavender', 'Roral Lavender'),
            ('Stone', 'Roral Stone'),
            ('Yellow', 'Roral Yellow'),
            ('Apricot', 'Roral Apricot'),
            ('Pink', 'Roral Pink'),
            ('Orange', 'Roral Orange'),
        )
         ),
    )
    os = models.CharField(max_length=1, choices=OS)
    internal_memory = models.CharField(max_length=3, choices=memory[4:])
    RAM = models.CharField(max_length=3, choices=memory[0:5])
#    camera = (range(1,25))
#    primary_camera = models.IntegerField(max_length=2, choices=camera)
    color = models.CharField(max_length=20, choices=COLORS)

    def __str__(self):
        return f" {self.Brand} {self.PhoneModel} {self.color} {self.internal_memory} {self.RAM}"
'''
class Products(models.Model):
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE)
    model_name = models.ForeignKey(Phones, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.set(brand_name)} {self.set(model_name)}"
'''
