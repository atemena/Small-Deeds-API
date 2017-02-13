from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


#calltoactions:
#Deeds:
	#Money
	#Show-up
	#Solidarity/Awareness
	#Education

class Deed(models.Model):
	title = models.CharField(max_length=63, db_index=True)
	description = models.TextField(blank=True, db_index=True)
	impact = models.IntegerField(blank=True, db_index=True)
	type = models.IntegerField(default=0, editable=False, db_index=True)
	inactive_pledges = models.IntegerField(default=0, db_index=True)
	active_pledges = models.IntegerField(default=0, db_index=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Pledge(models.Model):
	user = models.ForeignKey(User)
	deed = models.ForeignKey(Deed)
	threshold = models.IntegerField(default=0, db_index=True)
	active = models.BooleanField(default=False)

# class Donate(Deed):

# class ShowUp(Deed):
# 	address =
# 	time =

# class Awareness(Deed):
# 	action = 

# #can education be a subset of showing up?
# class Education(Deed):

# class Pledge(models.Model):
# 	user =
# 	deed =
# 	pledge =
# 	active =

