from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.

class myfiles(models.Model):
	filename =models.CharField(max_length=250, unique=True)
	time_of_uploading =models.DateTimeField(default=datetime.now, editable=False)
	type_of_file =models.CharField(max_length=250, blank=True)
	size =models.CharField(max_length=250)
	location =models.CharField(max_length=1000)
	new_file =models.FileField(null=True)

	def get_absolute_url(self):
		return reverse('display:details', kwargs={'pk':self.pk})

	def __str__(self):
		# return self.filename + ' + ' + self.type_of_file + ' + ' + self.size + ' + ' + self.location + ' + ' + unicode(self.time_of_uploading.strftime('%Y-%m-%d %H:%M:%S'))
		return self.filename + ' + ' +  unicode(self.time_of_uploading.strftime('%Y-%m-%d %H:%M'))