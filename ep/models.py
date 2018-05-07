from django.db import models
import datetime

# Create your models here.

class Event(models.Model):
	in_history = models.BooleanField(default=False, blank=True)
	cust_name = models.CharField(max_length=30)
	# Add customer email here
	# Require either email or customer phone number
	cust_phone = models.CharField(max_length=12, blank=True)
	event_date = models.DateField('event date')
	pickup_date = models.DateField('pickup date', blank=True)

	assoc_name = models.CharField(max_length=30)
	entry_date = models.DateField('date published', default=datetime.date.today, blank=True)

	#product_list = models.ManyToManyField(Event_Item, blank=True)

	total_amt = models.IntegerField('total drinks purchased', default=0, blank=True)
	total_cost = models.IntegerField('total $$ spent', default=0, blank=True)
	return_amt = models.IntegerField('total $$ returned', default=0, blank=True)

	#food_pairing = models.TextField()
	#cust_notes = models.TextField()
	#num_guests = models.IntegerField('number of gusts', default=0, blank=True)
	
class Event_Item(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	product_name = models.CharField(max_length=40, blank=True)
	product_size = models.IntegerField('size of item in mL/6-pack/case', blank=True)
	product_cost = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
	product_qty = models.IntegerField('Number of items purchased', blank=True)
