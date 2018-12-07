from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import resolvers
# Create your models here.

"""
class CheckboxInput():
    input_type = 'checkbox'
    template_name = 'django/forms/widgets/checkbox.html'

    def __init__(self, attrs=None, check_test=None):
        super().__init__(attrs)
        # check_test is a callable that takes a value and returns True
        # if the checkbox should be checked for that value.
        self.check_test = boolean_check if check_test is None else check_test

    def format_value(self, value):
        Only return the 'value' attribute if value isn't empty.
        if value is True or value is False or value is None or value == '':
            return
        return str(value)

    def get_context(self, name, value, attrs):
        if self.check_test(value):
            if attrs is None:
                attrs = {}
            attrs['checked'] = True
        return super().get_context(name, value, attrs)

    def value_from_datadict(self, data, files, name):
        if name not in data:
            # A missing value means False because HTML form submission does not
            # send results for unselected checkboxes.
            return False
        value = data.get(name)
        # Translate true and false strings to boolean values.
        values = {'true': True, 'false': False}
        if isinstance(value, str):
            value = cash4smartphonevalues.get(value.lower(), value)
        return bool(value)

    def value_omitted_from_data(self, data, files, name):
        # HTML checkboxes don't appear in POST data if not checked, so it's
        # never known if the value is actually omitted.
        return False


"""
class CatagoryManager(models.Manager):
    def create_Catagory(self, catagory):
        Catagory = self.create(catagory=catagory)
        return Catagory
'''
    catagory = models.CharField(max_length=20, primary=True)
    def __str__(self):
        return f"{self.catagory}"
'''
class Catagory(models.Model):
    catagory = models.CharField(max_length=20, primary_key=True)
    objects = CatagoryManager()
    def __str__(self):
        return self.catagory
#x = X.objects.create_X("Pride and Prejudice")

class BrandManager(models.Manager):
    def create_Brand(self, manufacturer):
        Brand = self.create(manufacturer=manufacturer)
        return Brand
    
class Brand(models.Model):
    manufacturer = models.CharField(max_length=40, primary_key=True)
    objects = BrandManager()
    def __str__(self):
        return self.manufacturer


class ProductManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute()
            result_list = []
'''          
            def create_Product(self, Catagory, Brand, PhoneModel):
                def __str__(self):
                    Catagory = self.catagory 
                    Brand = self.brand
                    PhoneModel = self.PhoneModel
                    Product = self.create_Product(self, catagory, brand, PhoneModel)
                    return PhoneModel

                    def __str__(self):
                        BrandManager = PhoneModel in brand
                        CatagoryManager = brand in Catagory
'''


class Product(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
#    catagory = models.ForeignKey(X, on_delete=models.CASCADE)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    PhoneModel = models.CharField(max_length=40, primary_key=True)
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
        return f"{self.Brand} {self.PhoneModel} {self.color} {self.internal_memory} {self.RAM}"
'''
class Products(models.Model):
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE)
    model_name = models.ForeignKey(Phones, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.set(brand_name)} {self.set(model_name)}"
'''
