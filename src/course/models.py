from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Subject(models.Model):
    class_title = models.CharField(max_length=500)
    class_description = models.CharField(max_length=1000)
    class_logo = models.CharField(max_length=500)
    class_level = models.IntegerField(default=0)
    class_category = models.CharField(max_length=50)







    #def get_absolute_url(self):
    #   return reverse('course:index', kwargs={'pk': self.pk})

    def __str__(self):
        return self.class_title

