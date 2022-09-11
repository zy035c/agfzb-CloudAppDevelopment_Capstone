from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=20, default='')
    description = models.CharField(null=False, max_length=2000, default='')

    def __str__(self):
        return self.name + "\n" + self.description 

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=20, default='')
    dealer_id = models.IntegerField()

    Sedan = 'Sedan'
    SUV = 'SUV'
    Wagon = 'Wagon'
    type_choices = [
        (Sedan, 'Sedan'),
        (SUV, 'SUV'),
        (Wagon, 'Wagon'),
    ]

    car_type = models.CharField(null=False, max_length=20, choices=type_choices, default=Wagon)
    year = models.DateField(null=True)

    def __str__(self):
        return "Model: " + self.name + "\nType: " + self.car_type + "\nYear: " + self.year.strftime('%Y')


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer(self, address, city, full_name, id_, lat, long_, short_name, st, zip_):
    self.address = address
    self.city = city
    self.full_name = full_name
    self.id_ = id_
    self.lat = lat
    self.long_ = long_
    self.short_name = short_name
    self.st = st
    self.zip_ = zip_
    
    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(self, dealership, id_, name, purchase, review, purchase_date, car_make, car_model, car_year):
    this.dealership = dealership
    this.id_ = id_
    this.name = name 
    this.purchase = purchase
    this.review = review 
    this.purchase_date = purchase_date
    this.car_make = car_make
    this.car_model = car_model
    this.car_year = car_year
    this.sentiment = None
    
    def __str__(self):
        return ""

