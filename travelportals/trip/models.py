from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from django.utils.text import slugify

# Create your models here.
from django.utils.translation import gettext_lazy as _
class Categories(models.Model):
	name=models.CharField( max_length=50)
	parent=models.CharField( max_length=50)

	

	class Meta:
		verbose_name = _("Categories")
		verbose_name_plural = _("Categoriess")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("Categories_detail", kwargs={"pk": self.pk})

def get_slug(instance):
   
    return slugify("{}".format(instance.name))

class Tour(models.Model):
	name=models.CharField( max_length=50,blank=True)
	Statu=models.CharField( max_length=50,blank=True,default="publish")
	slug = AutoSlugField(max_length=50, populate_from=get_slug, unique=False)
	date=models.DateField(auto_now_add=True)

	Categories=models.ManyToManyField(Categories)
  

	class Meta:
		verbose_name = _("Tour Categories")
		verbose_name_plural = _("Tour Categoriess")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("TourCategoriesdetail", kwargs={"pk": self.pk})


class Location(models.Model):
	city = models.CharField(max_length=30)
	region = models.CharField(max_length=2)
	image = models.ImageField(null=True)

    

class Review(models.Model):
	review = models.CharField(max_length=1000)
	rating = models.IntegerField()
	author = models.CharField(max_length=30)
	submissionDate = models.DateField()

class History(models.Model):
	userEmail = models.CharField(max_length=36)
	BOOKING_TYPES = [('flight', 'Flight'), ('train', 'Train'), ('hotel', 'Hotel')]
	bookingType = models.CharField(choices=BOOKING_TYPES, max_length=6)
	bookingStartDate = models.DateField()
	paymentAmount = models.DecimalField(max_digits=6,decimal_places=2)
	paymentCardNo = models.CharField(max_length=16)
	companyName = models.CharField(max_length=30, default='company')
	location = models.CharField(max_length=30, default='location')



class Flight(models.Model):
	companyName = models.CharField(max_length=30)
	sourceLocation = models.CharField(max_length=30)
	destinationLocation = models.CharField(max_length=30)
	departureDate = models.DateField()
	departureTime = models.TimeField()
	fareEconomy = models.DecimalField(max_digits=6,decimal_places=2)
	fareBusiness = models.DecimalField(max_digits=6,decimal_places=2)
	fareFirst = models.DecimalField(max_digits=6,decimal_places=2)
	numSeatsRemainingEconomy = models.IntegerField()
	numSeatsRemainingBusiness = models.IntegerField()
	numSeatsRemainingFirst = models.IntegerField()



class Train(models.Model):
	companyName = models.CharField(max_length=30)
	sourceLocation = models.CharField(max_length=30)
	destinationLocation = models.CharField(max_length=30)
	departureDate = models.DateField()
	departureTime = models.TimeField()
	fareEconomy = models.DecimalField(max_digits=6,decimal_places=2)
	fareBusiness = models.DecimalField(max_digits=6,decimal_places=2)
	fareFirst = models.DecimalField(max_digits=6,decimal_places=2)
	numSeatsRemainingEconomy = models.IntegerField()
	numSeatsRemainingBusiness = models.IntegerField()
	numSeatsRemainingFirst = models.IntegerField()    




class Hotel(models.Model):
	dailyCost = models.DecimalField(max_digits=6,decimal_places=2)
	address = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	companyName = models.CharField(max_length=30,default='hotel')   



class Payment(models.Model):
	PAYMENT_TYPES = [('credit', 'Credit'), ('debit', 'Debit')]
	amount = models.DecimalField(max_digits=6,decimal_places=2)
	paymentType = models.CharField(choices=PAYMENT_TYPES, max_length=6)
	cardNo = models.CharField(max_length=16)     






class Attraction(models.Model):
	location = models.ManyToManyField(Location)
	attractionName = models.CharField(unique=True,max_length=30)
	attractionDescription = models.CharField(max_length=1000)
	image = models.ImageField(null=True)
	

# class Purchase(models.Model):
# 	userID = models.ForeignKey(User, on_delete=models.DO_NOTHING, primary_key=True)
# 	bookingID = models.IntegerField()
# 	paymentID = models.IntegerField()